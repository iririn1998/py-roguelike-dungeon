import dungeon

# ダンジョン生成パラメータ
MAZE_WIDTH = 9    # 基本迷路の幅（5以上の奇数である必要があります）
MAZE_HEIGHT = 7   # 基本迷路の高さ（5以上の奇数である必要があります）
DUNGEON_SCALE = 5 # ダンジョンのスケール（拡大倍率）。3以上の奇数である必要があります。
                  # 実際のダンジョンサイズは (MAZE_WIDTH × DUNGEON_SCALE) × (MAZE_HEIGHT × DUNGEON_SCALE) になります

maze = dungeon.Maze.make_dungeon(MAZE_WIDTH, MAZE_HEIGHT, DUNGEON_SCALE)
dungeon.Maze.print_maze(maze)
