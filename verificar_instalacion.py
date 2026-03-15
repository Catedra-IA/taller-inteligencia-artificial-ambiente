#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de verificacion de instalacion del ambiente para Taller de IA.
Testea que todas las dependencias necesarias esten correctamente instaladas.
"""

import sys
import importlib
import locale
from typing import List, Tuple

# Detectar si podemos usar caracteres Unicode
def supports_unicode():
    """Detecta si el sistema soporta caracteres Unicode."""
    try:
        encoding = sys.stdout.encoding or locale.getpreferredencoding()
        # Intentar codificar un checkmark
        '✓'.encode(encoding)
        return True
    except (UnicodeEncodeError, AttributeError):
        return False

USE_UNICODE = supports_unicode()

# Símbolos según soporte Unicode
if USE_UNICODE:
    CHECK = '✓'
    CROSS = '✗'
else:
    CHECK = '[OK]'
    CROSS = '[X]'

# Colores para output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def check_import(module_name: str, package_name: str = None) -> Tuple[bool, str]:
    """
    Intenta importar un módulo y retorna si fue exitoso junto con info de versión.

    Args:
        module_name: nombre del módulo a importar
        package_name: nombre alternativo del paquete (ej: 'PIL' vs 'pillow')

    Returns:
        (success, version_info)
    """
    try:
        module = importlib.import_module(module_name)
        version = getattr(module, '__version__', 'sin versión disponible')
        return True, version
    except ImportError as e:
        return False, str(e)

def main():
    print(f"\n{BLUE}{'='*60}")
    print("  Verificacion de Instalacion - Taller de IA")
    print(f"{'='*60}{RESET}\n")

    # Lista de dependencias a verificar
    dependencies = [
        ("numpy", "NumPy"),
        ("matplotlib", "Matplotlib"),
        ("gymnasium", "Gymnasium"),
        ("pygame", "Pygame"),
        ("moviepy", "MoviePy"),
        ("tqdm", "tqdm"),
        ("IPython", "IPython"),
        ("jupyter", "Jupyter"),
        ("notebook", "Jupyter Notebook"),
    ]

    all_ok = True
    results = []

    print(f"{YELLOW}Verificando dependencias principales...{RESET}\n")

    for module_name, display_name in dependencies:
        success, info = check_import(module_name)
        results.append((display_name, success, info))

        if success:
            print(f"  {GREEN}{CHECK}{RESET} {display_name:<20} {GREEN}OK{RESET} (v{info})")
        else:
            print(f"  {RED}{CROSS}{RESET} {display_name:<20} {RED}FALTA{RESET}")
            all_ok = False

    # Verificar Python version
    print(f"\n{YELLOW}Verificando version de Python...{RESET}\n")
    py_version = sys.version_info
    if py_version.major == 3 and py_version.minor >= 10:
        print(f"  {GREEN}{CHECK}{RESET} Python {py_version.major}.{py_version.minor}.{py_version.micro} {GREEN}OK{RESET}")
    else:
        print(f"  {RED}{CROSS}{RESET} Python {py_version.major}.{py_version.minor}.{py_version.micro} {RED}(Se recomienda Python 3.10+){RESET}")
        all_ok = False

    # Test basico de funcionalidad
    print(f"\n{YELLOW}Ejecutando tests basicos...{RESET}\n")

    try:
        import numpy as np
        test_array = np.array([1, 2, 3])
        assert test_array.sum() == 6
        print(f"  {GREEN}{CHECK}{RESET} NumPy funciona correctamente")
    except Exception as e:
        print(f"  {RED}{CROSS}{RESET} Error en NumPy: {e}")
        all_ok = False

    try:
        import matplotlib
        matplotlib.use('Agg')  # Backend sin GUI para testing
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        plt.close(fig)
        print(f"  {GREEN}{CHECK}{RESET} Matplotlib funciona correctamente")
    except Exception as e:
        print(f"  {RED}{CROSS}{RESET} Error en Matplotlib: {e}")
        all_ok = False

    try:
        import gymnasium as gym
        # Test simple sin dependencias complejas
        env = gym.make('CartPole-v1')
        env.reset()
        env.close()
        print(f"  {GREEN}{CHECK}{RESET} Gymnasium funciona correctamente")
    except Exception as e:
        print(f"  {RED}{CROSS}{RESET} Error en Gymnasium: {e}")
        all_ok = False

    try:
        import subprocess
        result = subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"  {GREEN}{CHECK}{RESET} FFmpeg disponible")
        else:
            print(f"  {RED}{CROSS}{RESET} FFmpeg no responde correctamente")
            all_ok = False
    except FileNotFoundError:
        print(f"  {RED}{CROSS}{RESET} FFmpeg no encontrado (necesario para grabar videos)")
        all_ok = False
    except Exception as e:
        print(f"  {RED}{CROSS}{RESET} Error verificando FFmpeg: {e}")
        all_ok = False

    # Resumen final
    print(f"\n{BLUE}{'='*60}{RESET}\n")

    if all_ok:
        print(f"{GREEN}{CHECK} ¡Todas las dependencias están correctamente instaladas!{RESET}")
        print(f"\n{YELLOW}Puedes comenzar a trabajar con las notebooks del curso.{RESET}")
        print(f"\nPara iniciar Jupyter, ejecuta:")
        print(f"  {BLUE}jupyter notebook{RESET}")
        return 0
    else:
        print(f"{RED}{CROSS} Faltan algunas dependencias o hay errores.{RESET}")
        print(f"\n{YELLOW}Para instalar el ambiente completo, ejecuta:{RESET}")
        print(f"  {BLUE}conda env create -f environment.yml{RESET}")
        print(f"  {BLUE}conda activate taller-ia{RESET}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
