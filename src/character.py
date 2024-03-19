import pygame


class Player:
	"""
	Player instance

	Manages the movement and attributes of the player

	"""
	def __init__(self, spawn_location: list = (0, 0, 16, 16), **kwargs):
		# player specific attributes

		self.regen = 0.5
		self.max_hp = 100
		self.air_time = 0
		self.hp = self.max_hp
		self.alive: bool = False
		self.velocity_cap = 1.775
		self.linear_travel_speed = 0.5
		self.velocity_vector = pygame.Vector2(0, 0)

		# player animation attributes

		self.run_count: int = 0
		self.facing_right = True
		self.idle_count: int = 0
		self.jump_count: int = 0
		self.idle_animation = self.run_animation = self.jump_animation = []  # will be written later
		self.hitbox: pygame.Rect = pygame.Rect(*spawn_location)

		for k, v in kwargs.items():
			if hasattr(self, k):
				setattr(self, k, v)

	def _collision_test(self, tiles):
		colliding_tiles = []

		for tile in tiles:
			if self.hitbox.colliderect(tile):
				colliding_tiles.append(tile)

		return colliding_tiles

	def move(self, collision_types, movement_data, tile_data):
		self.hitbox.x += movement_data[0]

		for collision in self._collision_test(tile_data):
			if movement_data[0] > 0:
				self.hitbox.right = collision.left
				collision_types['right'] = True

			elif movement_data[0] < 0:
				self.hitbox.left = collision.right
				collision_types['left'] = True

		self.hitbox.y += movement_data[1]

		for collision in self._collision_test(tile_data):
			if movement_data[1] > 0:
				self.hitbox.bottom = collision.top
				collision_types['bottom'] = True

			elif movement_data[1] < 0:
				self.hitbox.top = collision.bottom
				collision_types['top'] = True

		return collision_types

	def update_pos(self, x, y):
		self.hitbox.x = x
		self.hitbox.y = y

	def update(self):
		if self.hp > self.max_hp:
			self.hp = self.max_hp

		if self.velocity_vector.x > self.velocity_cap:
			self.velocity_vector.x = self.velocity_cap

		if self.velocity_vector.y > 7.8:  # gravity cap
			self.velocity_vector.y = 7.8

		self.alive = self.hp > 0

		if self.idle_count + 2 >= len(self.idle_animation):
			self.idle_count = 0

		if self.run_count + 2 >= len(self.run_animation):
			self.run_count = 0

		if self.jump_count + 2 >= len(self.jump_animation):
			self.jump_count = 0

		self.hp += self.regen

	def reset(self, coordinates=(0, 0)):
		self.air_time = 0
		self.hp = self.max_hp
		self.facing_right = True
		self.update_pos(*coordinates)
