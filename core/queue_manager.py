from collections import deque
import logging

LOG = logging.getLogger(__name__)

class MusicQueueManager:
    """
    Manages the music download and upload queue for group chats.
    Each chat has its own queue.
    """
    def __init__(self):
        # {chat_id: deque([{'query': str, 'message': Message}])}
        self.queues = {}
        # {chat_id: bool} - True if a song is currently being processed
        self.is_processing = {}

    def add_to_queue(self, chat_id: int, query: str, message):
        """Adds a song request to the chat's queue."""
        if chat_id not in self.queues:
            self.queues[chat_id] = deque()
            self.is_processing[chat_id] = False
        
        self.queues[chat_id].append({'query': query, 'message': message})
        LOG.info(f"Added '{query}' to queue for chat {chat_id}. Queue size: {len(self.queues[chat_id])}")
        return len(self.queues[chat_id])

    def get_next_in_queue(self, chat_id: int):
        """Retrieves the next song request from the queue."""
        if chat_id in self.queues and self.queues[chat_id]:
            return self.queues[chat_id].popleft()
        return None

    def is_queue_empty(self, chat_id: int):
        """Checks if the queue for a chat is empty."""
        return chat_id not in self.queues or not self.queues[chat_id]

    def get_queue_list(self, chat_id: int):
        """Returns a list of queries currently in the queue."""
        if chat_id in self.queues:
            return [item['query'] for item in self.queues[chat_id]]
        return []

    def set_processing_status(self, chat_id: int, status: bool):
        """Sets the processing status for a chat."""
        self.is_processing[chat_id] = status
        LOG.debug(f"Chat {chat_id} processing status set to {status}")

    def is_currently_processing(self, chat_id: int):
        """Checks if a song is currently being processed for a chat."""
        return self.is_processing.get(chat_id, False)

# Global instance of the queue manager
queue_manager = MusicQueueManager()
