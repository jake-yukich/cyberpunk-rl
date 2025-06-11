"""Base environment class for reinforcement learning."""
from abc import ABC, abstractmethod
from typing import Any, Dict, Tuple, Optional
import numpy as np


class Environment(ABC):
    """Abstract base class for RL environments."""
    
    def __init__(self):
        self.action_space = None
        self.observation_space = None
        self.current_step = 0
        self.max_steps = 1000
        
    @abstractmethod
    def reset(self) -> np.ndarray:
        """Reset environment to initial state and return initial observation."""
        self.current_step = 0
        pass
        
    @abstractmethod
    def step(self, action: Any) -> Tuple[np.ndarray, float, bool, Dict]:
        """
        Execute action and return:
        - observation: next state
        - reward: reward for this transition
        - done: whether episode has ended
        - info: additional information
        """
        self.current_step += 1
        pass
        
    @abstractmethod
    def render(self, mode: str = 'human') -> Optional[np.ndarray]:
        """Render the environment."""
        pass
        
    def close(self):
        """Clean up resources."""
        pass
        
    @property
    def is_terminal(self) -> bool:
        """Check if we've reached terminal state."""
        return self.current_step >= self.max_steps