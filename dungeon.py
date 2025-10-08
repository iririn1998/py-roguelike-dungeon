import random

### 迷路を作るクラス ###
class Maze:
	OUT  = -1
	ROAD =  0
	WALL =  1
	ROOM =  2
	
	@staticmethod
	def make_maze(width, height):
		# 方向( 上・下・右・左 )
		dir = [[0, -1], [0, 1], [1, 0], [-1, 0]]
		# 配列をすべて道で初期化
		maze = [[Maze.ROAD for i in range(width)] for j in range(height)]
		# 周囲を壁で囲む
		for x in range(width):
			maze[0][x] = Maze.WALL
			maze[height - 1][x] = Maze.WALL
		for y in range(height):
			maze[y][0] = Maze.WALL
			maze[y][width - 1] = Maze.WALL
		# 柱を立てる・柱を拡張
		for y in range(2, height - 2, 2):
			for x in range(2, width - 2, 2):
				maze[y][x] = Maze.WALL
				d = random.randint(0, 3)
				if x > 2:
					d = random.randint(0, 2)
				maze[y + dir[d][1]][x + dir[d][0]] = Maze.WALL
		return maze
	
	@staticmethod
	def make_dungeon(width, height, scale = 3):
		# 引数に条件を設ける
		if width % 2 == 0 or height % 2 == 0 or width < 5 or height < 5:
			print("error:")
			print("make_dungeon(width, height, scale)のwidth, heightは5以上の奇数にしてください")
			exit(1)
		if scale % 2 == 0 or scale < 3:
			print("error:")
			print("make_dungeon(width, height, scale)のscaleは3以上の奇数にしてください")
			exit(1)
		# 元になる迷路を生成
		maze = Maze.make_maze(width, height)
		# 配列をすべて壁で初期化
		dungeon_width = width * scale
		dungeon_height = height * scale
		dungeon = [[Maze.WALL for i in range(dungeon_width)] for j in range(dungeon_height)]
		# 部屋と通路を配置
		dir = [[0, -1], [0, 1], [1, 0], [-1, 0]]
		for y in range(height):
			for x in range(width):
				dx = x * scale + int(scale / 2)
				dy = y * scale + int(scale / 2)
				if maze[y][x] == Maze.ROAD:
					if random.randint(0, 99) < 20:
						for ry in range(-int(scale / 2), int(scale / 2) + 1):
							for rx in range(-int(scale / 2), int(scale / 2) + 1):
								dungeon[dy + ry][dx + rx] = Maze.ROOM
					else:
						dungeon[dy][dx] = Maze.ROAD
						for i in range(4):
							if maze[y + dir[i][1]][x + dir[i][0]] == Maze.ROAD:
								for j in range(int(scale / 2)):
									dungeon[dy + (dir[i][1] * (j + 1))][dx + (dir[i][0] * (j + 1))] = Maze.ROAD
		return dungeon
	
	@staticmethod
	def print_maze(maze):
		width = len(maze[0])
		height = len(maze)
		print("----------------------")
		print()
		print("高さ：" + str(height))
		print("幅  ：" + str(width))
		print()
		for y in range(height):
			for x in range(width):
				match maze[y][x]:
					case Maze.ROAD:
						print("　", end = "")
					case Maze.WALL:
						print("⬛︎", end = "")
					case Maze.ROOM:
						print("　", end = "")
			print()
		print()
		print("----------------------")