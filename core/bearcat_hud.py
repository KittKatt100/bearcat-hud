import pandas as pd

class BearcatHUD:
    def __init__(self):
        try:
            self.games = {
                "Game 1": {
                    "Q1": [
                        {"play": "Run Left", "yards": 5},
                        {"play": "Pass Right", "yards": 12}
                    ],
                    "Q2": [
                        {"play": "Run Center", "yards": 3},
                        {"play": "Pass Deep", "yards": 25}
                    ]
                },
                "Game 2": {
                    "Q1": [
                        {"play": "Run Right", "yards": 7},
                        {"play": "Pass Left", "yards": 8}
                    ],
                    "Q2": [
                        {"play": "Pass Short", "yards": 4},
                        {"play": "Run Sweep", "yards": 9}
                    ]
                }
            }
        except Exception as e:
            print(f"❌ Error loading game data: {e}")
            self.games = {}

    def get_game_list(self):
        try:
            return list(self.games.keys())
        except Exception as e:
            print(f"❌ Error getting game list: {e}")
            return []

    def get_quarters(self, game):
        try:
            return list(self.games.get(game, {}).keys())
        except Exception as e:
            print(f"❌ Error getting quarters for {game}: {e}")
            return []

    def get_plays(self, game, quarter):
        try:
            plays = self.games.get(game, {}).get(quarter, [])
            return pd.DataFrame(plays)
        except Exception as e:
            print(f"❌ Error getting plays for {game} Q{quarter}: {e}")
            return pd.DataFrame()
