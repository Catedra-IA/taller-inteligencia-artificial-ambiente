#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de verificacion de instalacion del ambiente para Taller de IA.
Testea las dependencias necesarias para cada clase del curso.
(No incluye PyTorch ni dependencias del obligatorio)
"""

import sys
import importlib
import locale
import os
import tempfile
import shutil
from typing import Tuple

# Detectar si podemos usar caracteres Unicode
def supports_unicode():
    """Detecta si el sistema soporta caracteres Unicode."""
    try:
        encoding = sys.stdout.encoding or locale.getpreferredencoding()
        '✓'.encode(encoding)
        return True
    except (UnicodeEncodeError, AttributeError):
        return False

USE_UNICODE = supports_unicode()

if USE_UNICODE:
    CHECK = '✓'
    CROSS = '✗'
    WARN = '⚠'
else:
    CHECK = '[OK]'
    CROSS = '[X]'
    WARN = '[!]'

GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'


def ok(msg):
    print(f"  {GREEN}{CHECK}{RESET} {msg}")

def fail(msg):
    print(f"  {RED}{CROSS}{RESET} {msg}")

def warn(msg):
    print(f"  {YELLOW}{WARN}{RESET} {msg}")

def section(msg):
    print(f"\n{YELLOW}{msg}{RESET}\n")


def check_import(module_name: str) -> Tuple[bool, str]:
    try:
        module = importlib.import_module(module_name)
        version = getattr(module, '__version__', 'ok')
        return True, version
    except ImportError as e:
        return False, str(e)


def main():
    print(f"\n{BLUE}{'='*60}")
    print("  Verificacion de Instalacion - Taller de IA")
    print(f"{'='*60}{RESET}")

    all_ok = True
    warnings = []

    # ── Python ──────────────────────────────────────────────
    section("Python")
    py = sys.version_info
    if py.major == 3 and py.minor >= 10:
        ok(f"Python {py.major}.{py.minor}.{py.micro}")
    else:
        fail(f"Python {py.major}.{py.minor}.{py.micro} (se recomienda 3.10+)")
        all_ok = False

    # ── Dependencias base ───────────────────────────────────
    section("Dependencias principales")
    deps = [
        ("numpy", "NumPy"),
        ("matplotlib", "Matplotlib"),
        ("gymnasium", "Gymnasium"),
        ("pygame", "Pygame"),
        ("moviepy", "MoviePy"),
        ("tqdm", "tqdm"),
        ("IPython", "IPython"),
        ("notebook", "Jupyter Notebook"),
    ]
    for mod, name in deps:
        success, info = check_import(mod)
        if success:
            ok(f"{name:<20} (v{info})")
        else:
            fail(f"{name:<20} FALTA")
            all_ok = False

    # ── FFmpeg ──────────────────────────────────────────────
    section("FFmpeg (necesario para grabar videos)")
    try:
        import subprocess
        result = subprocess.run(
            ['ffmpeg', '-version'], capture_output=True, text=True
        )
        if result.returncode == 0:
            first_line = result.stdout.split('\n')[0]
            ok(f"FFmpeg disponible ({first_line.strip()})")
        else:
            fail("FFmpeg no responde correctamente")
            all_ok = False
    except FileNotFoundError:
        fail("FFmpeg no encontrado")
        all_ok = False
    except Exception as e:
        fail(f"Error verificando FFmpeg: {e}")
        all_ok = False

    # ── Tests funcionales por clase ─────────────────────────
    section("Tests funcionales por clase")

    # -- Clase 01: K-Armed Bandits --
    print(f"  {BLUE}Clase 01 - Bandidos de K Brazos{RESET}")
    try:
        import numpy as np
        # Operaciones vectoriales usadas en los agentes
        q_values = np.zeros(10)
        action = np.argmax(q_values)
        q_values[action] += 0.1 * (1.0 - q_values[action])
        # random choices como en epsilon-greedy
        np.random.choice(10)
        ok("NumPy: operaciones vectoriales y random")
    except Exception as e:
        fail(f"NumPy: {e}")
        all_ok = False

    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        ax1.plot([1, 2, 3], [1, 2, 3])
        ax1.set_title("test")
        ax1.legend(["test"])
        plt.close(fig)
        ok("Matplotlib: subplots y graficos de lineas")
    except Exception as e:
        fail(f"Matplotlib: {e}")
        all_ok = False

    try:
        from tqdm import tqdm
        list(tqdm(range(10), disable=True))
        ok("tqdm: barras de progreso")
    except Exception as e:
        fail(f"tqdm: {e}")
        all_ok = False

    # -- Clase 02: Dynamic Programming --
    print(f"\n  {BLUE}Clase 02 - Programacion Dinamica{RESET}")
    try:
        import gymnasium as gym
        from gymnasium.wrappers import RecordEpisodeStatistics, RecordVideo
        ok("Gymnasium wrappers: RecordEpisodeStatistics, RecordVideo")
    except Exception as e:
        fail(f"Gymnasium wrappers: {e}")
        all_ok = False

    try:
        import pygame
        pygame.init()
        pygame.quit()
        ok("Pygame: init/quit (renderizado de GridWorld)")
    except Exception as e:
        fail(f"Pygame: {e}")
        all_ok = False

    # -- Clase 03: Monte Carlo --
    print(f"\n  {BLUE}Clase 03 - Metodos Monte Carlo{RESET}")
    try:
        import gymnasium as gym
        env = gym.make('Blackjack-v1')
        obs, info = env.reset()
        assert len(obs) == 3, "Blackjack obs should be tuple of 3"
        env.close()
        ok("Gymnasium: Blackjack-v1")
    except Exception as e:
        fail(f"Gymnasium Blackjack-v1: {e}")
        all_ok = False

    try:
        from collections import defaultdict
        Q = defaultdict(lambda: np.zeros(2))
        Q[(21, 10, False)][0] = 1.0
        ok("collections.defaultdict (Q-table)")
    except Exception as e:
        fail(f"collections.defaultdict: {e}")
        all_ok = False

    try:
        import matplotlib
        matplotlib.use('Agg')
        from mpl_toolkits.mplot3d import Axes3D
        import matplotlib.pyplot as plt
        import matplotlib.cm as cm
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(
            np.array([[0, 1], [0, 1]]),
            np.array([[0, 0], [1, 1]]),
            np.array([[0, 1], [1, 0]]),
            cmap=cm.coolwarm
        )
        plt.close(fig)
        ok("Matplotlib 3D: plot_surface con colormaps")
    except Exception as e:
        fail(f"Matplotlib 3D: {e}")
        all_ok = False

    # -- Clase 04: Temporal Difference --
    print(f"\n  {BLUE}Clase 04 - Diferencias Temporales{RESET}")
    try:
        import gymnasium as gym
        env = gym.make('CliffWalking-v1')
        obs, info = env.reset()
        env.close()
        ok("Gymnasium: CliffWalking-v1")
    except Exception as e:
        fail(f"Gymnasium CliffWalking-v1: {e}")
        all_ok = False

    try:
        from gymnasium.wrappers import TransformObservation
        ok("Gymnasium wrapper: TransformObservation")
    except Exception as e:
        fail(f"TransformObservation: {e}")
        all_ok = False

    # -- Clase 06: Dyna-Q --
    print(f"\n  {BLUE}Clase 06 - Planificacion Dyna-Q{RESET}")
    try:
        import gymnasium as gym
        env = gym.make('Taxi-v3')
        obs, info = env.reset()
        env.close()
        ok("Gymnasium: Taxi-v3")
    except Exception as e:
        fail(f"Gymnasium Taxi-v3: {e}")
        all_ok = False

    try:
        from IPython.display import Video, display
        ok("IPython.display: Video, display")
    except Exception as e:
        fail(f"IPython.display: {e}")
        all_ok = False

    # -- RecordVideo end-to-end --
    print(f"\n  {BLUE}RecordVideo (grabacion de episodios){RESET}")
    try:
        import gymnasium as gym
        from gymnasium.wrappers import RecordVideo
        tmpdir = tempfile.mkdtemp(prefix="taller_ia_test_")
        env = gym.make('CartPole-v1', render_mode='rgb_array')
        env = RecordVideo(env, video_folder=tmpdir, episode_trigger=lambda x: True)
        obs, info = env.reset()
        for _ in range(20):
            action = env.action_space.sample()
            obs, reward, terminated, truncated, info = env.step(action)
            if terminated or truncated:
                break
        env.close()
        # Verificar que se genero un video
        videos = [f for f in os.listdir(tmpdir) if f.endswith('.mp4')]
        shutil.rmtree(tmpdir, ignore_errors=True)
        if videos:
            ok("RecordVideo: grabo video correctamente")
        else:
            warn("RecordVideo: no se genero archivo .mp4 (puede requerir mas pasos)")
            warnings.append("RecordVideo no genero .mp4")
    except Exception as e:
        fail(f"RecordVideo: {e}")
        all_ok = False
        try:
            shutil.rmtree(tmpdir, ignore_errors=True)
        except Exception:
            pass

    # ── Resumen ─────────────────────────────────────────────
    print(f"\n{BLUE}{'='*60}{RESET}\n")

    if warnings:
        for w in warnings:
            warn(w)
        print()

    if all_ok:
        print(f"{GREEN}{CHECK} Todas las dependencias estan correctamente instaladas!{RESET}")
        print(f"\n  Para iniciar Jupyter:")
        print(f"  {BLUE}jupyter notebook{RESET}")
        return 0
    else:
        print(f"{RED}{CROSS} Faltan dependencias o hay errores.{RESET}")
        print(f"\n  Para instalar el ambiente completo:")
        print(f"  {BLUE}conda env create -f environment.yml{RESET}")
        print(f"  {BLUE}conda activate taller-ia{RESET}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
