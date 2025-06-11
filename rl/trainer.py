"""Training loop for reinforcement learning."""
from typing import Dict, List, Optional, Callable
import numpy as np
from collections import defaultdict
import time


class Trainer:
    """Main training loop for RL agents."""
    
    def __init__(self, env, agent, logger=None):
        self.env = env
        self.agent = agent
        self.logger = logger
        self.episode_rewards = []
        self.episode_lengths = []
        
    def train(self, 
              num_episodes: int,
              max_steps_per_episode: Optional[int] = None,
              eval_frequency: int = 100,
              eval_episodes: int = 10,
              save_frequency: int = 1000,
              save_path: Optional[str] = None,
              callbacks: Optional[List[Callable]] = None) -> Dict[str, List[float]]:
        """
        Train the agent for a specified number of episodes.
        
        Returns:
            Dictionary of training metrics
        """
        metrics = defaultdict(list)
        
        for episode in range(num_episodes):
            # Training episode
            episode_reward, episode_length = self._run_episode(
                training=True, 
                max_steps=max_steps_per_episode
            )
            
            metrics['train_reward'].append(episode_reward)
            metrics['train_length'].append(episode_length)
            
            # Evaluation
            if episode % eval_frequency == 0:
                eval_rewards = []
                self.agent.eval()
                for _ in range(eval_episodes):
                    reward, _ = self._run_episode(training=False, max_steps=max_steps_per_episode)
                    eval_rewards.append(reward)
                self.agent.train()
                
                avg_eval_reward = np.mean(eval_rewards)
                metrics['eval_reward'].append(avg_eval_reward)
                
                if self.logger:
                    self.logger(f"Episode {episode}: Train Reward: {episode_reward:.2f}, "
                              f"Eval Reward: {avg_eval_reward:.2f}")
                else:
                    print(f"Episode {episode}: Train Reward: {episode_reward:.2f}, "
                          f"Eval Reward: {avg_eval_reward:.2f}")
            
            # Save checkpoint
            if save_path and episode % save_frequency == 0:
                self.agent.save(f"{save_path}/checkpoint_{episode}.pkl")
                
            # Callbacks
            if callbacks:
                for callback in callbacks:
                    callback(episode, metrics)
                    
        return dict(metrics)
        
    def _run_episode(self, training: bool = True, max_steps: Optional[int] = None) -> Tuple[float, int]:
        """Run a single episode."""
        observation = self.env.reset()
        episode_reward = 0
        episode_length = 0
        done = False
        
        max_steps = max_steps or self.env.max_steps
        
        while not done and episode_length < max_steps:
            # Select action
            action = self.agent.act(observation)
            
            # Execute action
            next_observation, reward, done, info = self.env.step(action)
            
            # Store experience and learn
            if training:
                experience = {
                    'state': observation,
                    'action': action,
                    'reward': reward,
                    'next_state': next_observation,
                    'done': done
                }
                self.agent.learn(experience)
            
            episode_reward += reward
            episode_length += 1
            observation = next_observation
            
        return episode_reward, episode_length
        
    def evaluate(self, num_episodes: int = 100) -> Dict[str, float]:
        """Evaluate the agent's performance."""
        self.agent.eval()
        rewards = []
        lengths = []
        
        for _ in range(num_episodes):
            reward, length = self._run_episode(training=False)
            rewards.append(reward)
            lengths.append(length)
            
        self.agent.train()
        
        return {
            'mean_reward': np.mean(rewards),
            'std_reward': np.std(rewards),
            'mean_length': np.mean(lengths),
            'std_length': np.std(lengths)
        }