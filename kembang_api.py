import pygame
import random
import math

# Inisialisasi Pygame
pygame.init()

# Konfigurasi layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animasi Kembang Api")
clock = pygame.time.Clock()

# Warna kembang api
colors = [(255, 69, 0), (255, 140, 0), (255, 215, 0), (144, 238, 144), (0, 191, 255), (147, 112, 219), (255, 182, 193)]

# Class untuk partikel kembang api
class FireworkParticle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = random.choice(colors)
        self.size = random.randint(2, 4)
        self.life = 1.0
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(2, 6)
        self.gravity = 0.05

    def update(self):
        # Perbarui posisi partikel berdasarkan sudut dan kecepatan
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.speed *= 0.98
        self.y += self.gravity
        self.life -= 0.02

    def draw(self, screen):
        # Gambar partikel dengan efek fading
        if self.life > 0:
            faded_color = (
                int(self.color[0] * self.life),
                int(self.color[1] * self.life),
                int(self.color[2] * self.life),
            )
            pygame.draw.circle(screen, faded_color, (int(self.x), int(self.y)), self.size)

# Class untuk peluncur kembang api
class FireworkLauncher:
    def __init__(self):
        self.x = random.randint(100, WIDTH - 100)
        self.y = HEIGHT
        self.color = random.choice(colors)
        self.speed = random.uniform(5, 8)
        self.max_height = random.randint(150, HEIGHT // 2)
        self.exploded = False
        self.particles = []

    def update(self):
        # Naikkan peluncur jika belum meledak
        if not self.exploded:
            self.y -= self.speed
            self.speed -= 0.1
            if self.speed <= 0 or self.y <= self.max_height:
                self.explode()

        # Update partikel jika sudah meledak
        for particle in self.particles:
            particle.update()

    def explode(self):
        # Ubah status menjadi meledak dan buat partikel
        self.exploded = True
        self.particles = [FireworkParticle(self.x, self.y, self.color) for _ in range(100)]

    def draw(self, screen):
        # Gambar peluncur atau partikel ledakan
        if not self.exploded:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 5)
        else:
            for particle in self.particles:
                particle.draw(screen)

# List kembang api yang sedang aktif
fireworks = []

# Loop utama animasi
running = True
while running:
    screen.fill((0, 0, 0))

    # Tambah kembang api secara acak
    if random.randint(0, 50) == 1:
        fireworks.append(FireworkLauncher())

    # Update dan gambar setiap kembang api
    for firework in fireworks[:]:
        firework.update()
        firework.draw(screen)
        
        # Hapus kembang api jika semua partikel sudah hilang
        if firework.exploded and all(p.life <= 0 for p in firework.particles):
            fireworks.remove(firework)

    pygame.display.flip()
    clock.tick(30)

    # Event handling untuk keluar dari animasi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

