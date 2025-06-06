"""Game loop implementation for Cyberpunk RL."""

from enum import Enum, auto
import random

from board import Board
from gangs import Gang, TygerClaws, Valentinos, VoodooBoys, Maelstrom, Action
from units import Solo, Techie, Netrunner, Drone, Hideout

class GamePhase(Enum):
    ACTIVATE = auto()
    RECLAIM = auto()

class Turn:
    def __init__(self, player: Gang):
        self.player = player
        self.phase = GamePhase.ACTIVATE

    def execute_action(self, action: Action, game: 'Game'):
        """Execute a chosen action."""
        print(f"{self.player.name} chose {action.name}.")
        
        # Execute specific action logic
        if action == Action.ACTIVATE_SOLO:
            self._handle_activate_solo(game)
        elif action == Action.ACTIVATE_TECHIES:
            self._handle_activate_techies(game)
        elif action == Action.ACTIVATE_NETRUNNERS:
            self._handle_activate_netrunners(game)
        elif action == Action.UPGRADE_COMBAT_CARD:
            self._handle_upgrade_combat_card(game)
        elif action == Action.BUILD_HIDEOUT:
            self._handle_build_hideout(game)
        elif action == Action.ACTION_WILDCARD:
            self._handle_action_wildcard(game)
        else:
            print(f"Unknown action: {action.name}")
        
        # Move action from available to reclaim
        if action in self.player.actions["available"]:
            self.player.actions["available"].remove(action)
            self.player.actions["reclaim"].add(action)
        else:
            print(f"Warning: Action {action.name} not available for {self.player.name}")

    def _handle_activate_solo(self, game: 'Game'):
        """Handle solo activation with movement."""
        print(f"{self.player.name} is activating Solos.")
        
        # Get all solos belonging to this player
        solos = self.player.solos
        if not solos:
            print(f"{self.player.name} has no Solos to activate.")
            return
        
        # For now, move first solo to a random adjacent district (placeholder for player choice)
        solo = solos[0]
        current_district = solo.district
        if current_district and current_district in game.board.neighbors:
            adjacent_districts = list(game.board.neighbors[current_district])
            if adjacent_districts:
                target_district = adjacent_districts[0]  # Placeholder: would be player choice
                solo.move(target_district, game.board)
        
        # TODO: Add combat initiation logic

    def _handle_activate_techies(self, game: 'Game'):
        """Handle techie activation with movement."""
        print(f"{self.player.name} is activating Techies.")
        
        # Get all techies and drones belonging to this player
        techies = self.player.techies
        drones = self.player.drones
        moveable_units = techies + drones
        
        if not moveable_units:
            print(f"{self.player.name} has no Techies or Drones to activate.")
            return
        
        # For now, move first techie to a random adjacent district (placeholder for player choice)
        unit = moveable_units[0]
        current_district = unit.district
        if current_district and current_district in game.board.neighbors:
            adjacent_districts = list(game.board.neighbors[current_district])
            if adjacent_districts:
                target_district = adjacent_districts[0]  # Placeholder: would be player choice
                unit.move(target_district, game.board)
        
        # TODO: Add drone building, opportunity seizing, edgerunner hiring logic

    def _handle_upgrade_combat_card(self, game: 'Game'):
        """Placeholder for combat card upgrade logic."""
        print(f"{self.player.name} is upgrading a combat card.")
        # Add market interaction
        pass

    def _handle_activate_netrunners(self, game: 'Game'):
        """Handle netrunner activation with movement."""
        print(f"{self.player.name} is activating Netrunners.")
        
        # Get all netrunners belonging to this player
        netrunners = self.player.netrunners
        if not netrunners:
            print(f"{self.player.name} has no Netrunners to activate.")
            return
        
        # For now, move first netrunner to a random adjacent district (placeholder for player choice)
        netrunner = netrunners[0]
        current_district = netrunner.district
        if current_district and current_district in game.board.neighbors:
            adjacent_districts = list(game.board.neighbors[current_district])
            if adjacent_districts:
                target_district = adjacent_districts[0]  # Placeholder: would be player choice
                netrunner.move(target_district, game.board)
        
        # TODO: Add netrunning logic

    def _handle_build_hideout(self, game: 'Game'):
        """Placeholder for building hideout logic."""
        print(f"{self.player.name} is building a hideout.")
        # Add resource deduction, board update
        pass
    
    def _handle_action_wildcard(self, game: 'Game'):
        """Placeholder for wildcard action logic."""
        print(f"{self.player.name} is using a wildcard action.")
        pass


class Activate(Turn):
    def __init__(self, player: Gang):
        super().__init__(player)
        self.phase = GamePhase.ACTIVATE

    def run_phase(self, game: 'Game'):
        print(f"--- {self.player.name}'s Activate Phase ---")
        # Simple example: player chooses the first available action
        if self.player.actions["available"]:
            action_to_take = list(self.player.actions["available"])[0] # Player would normally choose
            print(f"{self.player.name} available actions: {[a.name for a in self.player.actions['available']]}")
            self.execute_action(action_to_take, game)
        else:
            print(f"{self.player.name} has no available actions for Activate phase.")


class Reclaim(Turn):
    def __init__(self, player: Gang):
        super().__init__(player)
        self.phase = GamePhase.RECLAIM

    def run_phase(self, game: 'Game'):
        print(f"--- {self.player.name}'s Reclaim Phase ---")
        # Move all actions from reclaim to available
        for action in list(self.player.actions["reclaim"]): # Iterate over a copy
            self.player.actions["reclaim"].remove(action)
            self.player.actions["available"].add(action)
        print(f"{self.player.name} reclaimed all actions.")
        # Placeholder for other reclaim phase logic (e.g., district dominance, market refresh)
        # game.board.check_district_dominance()
        # game.board.refresh_markets()


class Game:
    def __init__(self, num_players: int = 4, num_rounds: int = 5):
        if num_players != 4:
            # For now, fixing to 4 players as per the gang setup
            print("Warning: Game currently designed for 4 players (gangs).")
            num_players = 4
        
        self.board = Board(players=num_players)
        self.gang_names = [MAELSTROM, TYGER_CLAWS, VALENTINOS, VOODOO_BOYS] # From net.py or define centrally
        self.players: list[Gang] = []
        self.current_player_index: int = 0
        self.round: int = 1
        self.num_rounds = num_rounds # Max rounds
        self.game_over: bool = False

        self._setup_game()

    def _setup_game(self):
        print("Setting up the game...")
        # Initialize Gangs
        gang_classes = [Maelstrom, TygerClaws, Valentinos, VoodooBoys]
        if len(gang_classes) != len(self.gang_names): # Should be 4
            raise ValueError("Mismatch in number of gang types for setup.")

        for i in range(len(gang_classes)):
            gang_instance = gang_classes[i]()
            self.players.append(gang_instance)

        # Determine Starting Player
        self.current_player_index = random.randint(0, len(self.players) - 1)
        print(f"{self.players[self.current_player_index].name} will start the game.")
        
        # Distribute starting resources based on turn order
        # 1st and 2nd players: 2 eurodollars, 1 contraband
        # 3rd and 4th players: 2 eurodollars, 2 contraband
        turn_order = []
        for i in range(len(self.players)):
            player_index = (self.current_player_index + i) % len(self.players)
            turn_order.append(player_index)
            player = self.players[player_index]
            
            if i < 2:  # 1st and 2nd players
                player.eurodollars = 2
                player.contraband = 1
                print(f"{player.name} (position {i+1}) gets 2 eurodollars and 1 contraband")
            else:  # 3rd and 4th players
                player.eurodollars = 2
                player.contraband = 2
                print(f"{player.name} (position {i+1}) gets 2 eurodollars and 2 contraband")
        
        # Place starting units for each gang
        for gang in self.players:
            starting_district = self.board.districts[gang.starting_district]
            
            # Create and place units
            hideout = Hideout(gang)
            solo = Solo(gang)
            techie = Techie(gang)
            drone = Drone(gang)
            netrunner = Netrunner(gang)
            
            # Add units to gang's unit lists
            gang.hideouts.append(hideout)
            gang.solos.append(solo)
            gang.techies.append(techie)
            gang.drones.append(drone)
            gang.netrunners.append(netrunner)
            
            # Place units in starting district
            for unit in [hideout, solo, techie, drone, netrunner]:
                unit.district = starting_district.name
                starting_district.units.append(unit)
            
            # Update district presence
            starting_district.presence.append(gang.name)
            
            print(f"Placed {gang.name} units in {gang.starting_district}: 1 hideout, 1 solo, 1 techie, 1 drone, 1 netrunner")
        
        # Populate Markets - simplified
        print("Populating markets (simplified)...")
        # self.board.opportunities_market.deck = [Opportunity(...) , ...] # Populate with actual Opportunity objects
        # self.board.combat_upgrade_market.deck = [CombatUpgrade(...), ...]
        # self.board.edgerunners_market.deck = [Edgerunner(...), ...]
        # random.shuffle(self.board.opportunities_market.deck) # etc. for other markets

        print("Game setup complete.")

    def start_game_loop(self):
        print("\n--- Game Start ---")
        while not self.game_over and self.round <= self.num_rounds:
            print(f"\n=== Round {self.round} ===")
            for i in range(len(self.players)):
                current_player = self.players[self.current_player_index]
                if self.game_over: break

                print(f"\nIt's {current_player.name}'s turn.")

                # Activate Phase
                activate_phase = Activate(current_player)
                activate_phase.run_phase(self)

                # Reclaim Phase
                reclaim_phase = Reclaim(current_player)
                reclaim_phase.run_phase(self)
                
                # Check game end conditions after each player's full turn
                self._check_game_end_conditions()
                if self.game_over:
                    break

                self.current_player_index = (self.current_player_index + 1) % len(self.players)
            
            if not self.game_over:
                self.round += 1
        
        print("\n--- Game Over ---")
        self._declare_winner()

    def _check_game_end_conditions(self):
        # Example: Game ends if a player reaches X Street Cred (not implemented yet)
        # for player in self.players:
        #     if player.street_cred >= 10: # Arbitrary win condition
        #         self.game_over = True
        #         print(f"Game over! {player.name} reached the Street Cred goal.")
        #         return

        if self.round > self.num_rounds:
            self.game_over = True
            print("Game over! Maximum rounds reached.")
    
    def _declare_winner(self):
        # Simple winner declaration by Street Cred
        winner = max(self.players, key=lambda p: p.street_cred, default=None)
        if winner:
            print(f"{winner.name} wins with {winner.street_cred} Street Cred!")
        else:
            print("No winner could be determined.")

if __name__ == '__main__':
    # Constants for gang names - should ideally be imported or defined in a shared location
    MAELSTROM = "Maelstrom"
    TYGER_CLAWS = "Tyger Claws"
    VALENTINOS = "Valentinos"
    VOODOO_BOYS = "Voodoo Boys"
    
    game = Game(num_rounds=3) # Run for a few rounds for testing
    game.start_game_loop()

