from ex2 import strategy

aggressive = strategy.AggressiveStrategy
defensive = strategy.DefensiveStrategy
normal = strategy.NormalStrategy
strategies = strategy.BattleStrategy
battle_exception = strategy.BattleException

__all__ = ["aggressive", "defensive", "normal", "strategies",
           "battle_exception"]
