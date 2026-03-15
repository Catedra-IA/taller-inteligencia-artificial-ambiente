# Taller de Inteligencia Artificial - Ambiente de Desarrollo

[![Test Environment on Multiple OS](https://github.com/Catedra-IA/taller-inteligencia-artificial-ambiente/actions/workflows/test-environment.yml/badge.svg)](https://github.com/Catedra-IA/taller-inteligencia-artificial-ambiente/actions/workflows/test-environment.yml)

Ambiente de desarrollo multiplataforma para el Taller de Inteligencia Artificial. Este repositorio contiene el archivo de configuración de conda y scripts de verificación testeados en **Windows**, **macOS** y **Linux** mediante GitHub Actions.

## 🎯 Propósito

Este repositorio público proporciona:

1. **Archivo de ambiente conda** (`environment.yml`) - Configuración reproducible de dependencias
2. **Script de verificación** (`verificar_instalacion.py`) - Validación automática de la instalación
3. **Testing automatizado** - CI/CD con GitHub Actions en 3 sistemas operativos

## 📦 ¿Qué incluye?

El ambiente `taller-ia` incluye las siguientes dependencias:

- **Python 3.12**
- **NumPy** >= 1.24, < 2.0 - Computación numérica
- **Matplotlib** >= 3.7 - Visualización y gráficos 3D
- **Gymnasium** >= 1.0 - Ambientes de Reinforcement Learning
- **Pygame** >= 2.1 - Rendering de ambientes personalizados
- **MoviePy** - Creación de videos (para RecordVideo wrapper)
- **FFmpeg** - Codificación de videos
- **Jupyter** - Notebooks interactivas
- **tqdm** - Barras de progreso

**Nota:** Este ambiente **NO incluye PyTorch** ni otras dependencias del trabajo obligatorio. Es específicamente para seguir las clases.

## 🚀 Instalación Rápida

### Requisitos Previos

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) o [Anaconda](https://www.anaconda.com/download) instalado

### Pasos

```bash
# 1. Crear el ambiente desde el repositorio remoto
conda env create -f https://raw.githubusercontent.com/Catedra-IA/taller-inteligencia-artificial-ambiente/main/environment.yml

# 2. Activar el ambiente
conda activate taller-ia

# 3. Verificar la instalación
curl -O https://raw.githubusercontent.com/Catedra-IA/taller-inteligencia-artificial-ambiente/main/verificar_instalacion.py
python verificar_instalacion.py
```

Si todo está correcto, verás ✓ en verde para todas las dependencias.

## ✅ Testing Automatizado

Este repositorio utiliza GitHub Actions para testear automáticamente el ambiente en:

- ✅ **Ubuntu** (latest)
- ✅ **macOS** (latest) - Intel y ARM (M1/M2/M3)
- ✅ **Windows** (latest)

### Qué se testea

1. Creación del ambiente conda
2. Instalación de todas las dependencias
3. Imports de cada librería
4. Funcionalidad básica de NumPy, Matplotlib y Gymnasium
5. Ejecución del script de verificación

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

## 📧 Contacto

Para preguntas sobre el ambiente o problemas de instalación, abre un [issue](https://github.com/Catedra-IA/taller-inteligencia-artificial-ambiente/issues).
