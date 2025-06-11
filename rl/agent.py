"""Base agent class for reinforcement learning."""
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Tuple
import numpy as np


class Agent(ABC):
    """Abstract base class for RL agents."""
    
    def __init__(self, action_space, observation_space, learning_rate: float = 0.001):
        self.action_space = action_space
        self.observation_space = observation_space
        self.learning_rate = learning_rate
        self.training = True
        
    @abstractmethod
    def act(self, observation: np.ndarray) -> Any:
        """Select action given current observation."""
        pass
        
    @abstractmethod
    def learn(self, experiences: Dict) -> Dict[str, float]:
        """Update agent based on experiences. Return metrics."""
        pass
        
    def train(self):
        """Set agent to training mode."""
        self.training = True
        
    def eval(self):
        """Set agent to evaluation mode."""
        self.training = False
        
    def save(self, path: str):
        """Save agent parameters."""
        pass
        
    def load(self, path: str):
        """Load agent parameters."""
        pass


class ReplayBuffer:
    """Experience replay buffer for off-policy learning."""
    
    def __init__(self, capacity: int = 10000):
        self.capacity = capacity
        self.buffer = []
        self.position = 0
        
    def push(self, state, action, reward, next_state, done):
        """Store a transition."""
        if len(self.buffer) < self.capacity:
            self.buffer.append(None)
        self.buffer[self.position] = (state, action, reward, next_state, done)
        self.position = (self.position + 1) % self.capacity
        
    def sample(self, batch_size: int) -> List[Tuple]:
        """Sample a batch of transitions."""
        indices = np.random.choice(len(self.buffer), batch_size, replace=False)
        return [self.buffer[i] for i in indices]
        
    def __len__(self):
        return len(self.buffer)