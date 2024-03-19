import os

import pygame


def _load_image(img_name):
	return pygame.image.load(img_name).convert_alpha()


class Gallery:
	def __init__(self):
		self.player_run_images = []
		self.player_jump_images = []
		self.player_idle_images = []

		for i in range(1, 6):
			idle_img = _load_image(os.path.join('assets', 'player', 'idle_images', 'idle_' + str(i) + '.png'))
			self.player_idle_images.append(idle_img)

		for i in range(1, 8):
			run_img = _load_image(os.path.join('assets', 'player', 'run_images', 'run_' + str(i) + '.png'))
			self.player_run_images.append(run_img)

		for i in range(1, 1):
			jump_img = _load_image(os.path.join('assets', 'player', 'jump_images', 'jump_' + str(i) + '.png'))
			self.player_jump_imgages.append(jump_img)

		self.player_run_animation = self._animate(self.player_run_images, 16)
		self.player_idle_animation = self._animate(self.player_idle_images, 96)
		self.player_jump_animation = self._animate(self.player_jump_images, 16)

	@staticmethod
	def _animate(frames, frame_duration):
		animation = []
		
		for u in range(len(frames)):
			for v in range(frame_duration):
				animation.append(frames[u])

		return animation
