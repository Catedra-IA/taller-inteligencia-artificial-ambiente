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

- **Python 3.11**
- **NumPy** >= 1.24, < 2.0 - Computación numérica
- **Matplotlib** >= 3.7 - Visualización
- **Gymnasium** >= 0.29 - Ambientes de Reinforcement Learning
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

## 🔧 Instalación Local (desarrollo)

Si tienes el repositorio clonado localmente:

```bash
# Clonar el repositorio
git clone https://github.com/Catedra-IA/taller-inteligencia-artificial-ambiente.git
cd taller-inteligencia-artificial-ambiente

# Crear el ambiente
conda env create -f environment.yml

# Activar
conda activate taller-ia

# Verificar
python verificar_instalacion.py
```

## ✅ Testing Automatizado

Este repositorio utiliza GitHub Actions para testear automáticamente el ambiente en:

- ✅ **Ubuntu** (latest)
- ✅ **macOS** (latest) - Intel y ARM (M1/M2/M3)
- ✅ **Windows** (latest)

Los tests se ejecutan:
- En cada push a `main`
- En cada pull request
- Semanalmente los lunes a las 9:00 UTC
- Manualmente vía workflow dispatch

### Qué se testea

1. Creación del ambiente conda
2. Instalación de todas las dependencias
3. Imports de cada librería
4. Funcionalidad básica de NumPy, Matplotlib y Gymnasium
5. Ejecución del script de verificación

## 🔄 Uso en Otros Repositorios

Para referenciar este ambiente desde otros repositorios (como el repositorio privado de las clases):

### Opción 1: URL directa

```bash
conda env create -f https://raw.githubusercontent.com/Catedra-IA/taller-inteligencia-artificial-ambiente/main/environment.yml
```

### Opción 2: Submódulo de Git

```bash
# En el repositorio que quiera usar este ambiente
git submodule add https://github.com/Catedra-IA/taller-inteligencia-artificial-ambiente.git ambiente
cd ambiente
conda env create -f environment.yml
```

### Opción 3: Documentación con enlace

En el README del proyecto:

```markdown
## Instalación

El ambiente de desarrollo está definido en el [repositorio público de ambiente](https://github.com/Catedra-IA/taller-inteligencia-artificial-ambiente).

\`\`\`bash
conda env create -f https://raw.githubusercontent.com/Catedra-IA/taller-inteligencia-artificial-ambiente/main/environment.yml
conda activate taller-ia
\`\`\`
```

## 🛠️ Solución de Problemas

### El ambiente no se crea correctamente

```bash
# Actualizar conda
conda update conda

# Limpiar cache
conda clean --all

# Intentar nuevamente
conda env create -f environment.yml
```

### Errores en macOS ARM (M1/M2/M3)

```bash
# Forzar arquitectura x86
CONDA_SUBDIR=osx-64 conda env create -f environment.yml
```

### Jupyter no encuentra el kernel

```bash
conda activate taller-ia
python -m ipykernel install --user --name=taller-ia --display-name="Taller IA"
```

## 📊 Estado de los Tests

Puedes ver el estado actual de los tests en diferentes plataformas en la [página de Actions](https://github.com/Catedra-IA/taller-inteligencia-artificial-ambiente/actions).

## 🤝 Contribuir

Para sugerir cambios al ambiente:

1. Fork este repositorio
2. Crea una rama con tus cambios
3. Testea localmente en tu sistema operativo
4. Abre un Pull Request
5. Los tests automáticos verificarán la compatibilidad multiplataforma

## 📝 Actualizar el Ambiente

Para usuarios que ya tienen el ambiente instalado:

```bash
conda activate taller-ia
conda env update -f https://raw.githubusercontent.com/Catedra-IA/taller-inteligencia-artificial-ambiente/main/environment.yml --prune
```

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

## 📧 Contacto

Para preguntas sobre el ambiente o problemas de instalación, abre un [issue](https://github.com/Catedra-IA/taller-inteligencia-artificial-ambiente/issues).
