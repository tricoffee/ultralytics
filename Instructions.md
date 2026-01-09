## Installation

pip install -e .

## Installation LOG

(base) C:\Users\lihen>cd C:\HeLHDev\ultralytics

(base) C:\HeLHDev\ultralytics>pip install -e .
Obtaining file:///C:/HeLHDev/ultralytics
Installing build dependencies ... done
Checking if build backend supports build_editable ... done
Getting requirements to build editable ... done
Preparing editable metadata (pyproject.toml) ... done
Requirement already satisfied: numpy>=1.23.0 in c:\users\lihen\anaconda3\lib\site-packages (from ultralytics==8.3.234) (2.1.3)
Requirement already satisfied: matplotlib>=3.3.0 in c:\users\lihen\anaconda3\lib\site-packages (from ultralytics==8.3.234) (3.10.0)
Collecting opencv-python>=4.6.0 (from ultralytics==8.3.234)
Downloading opencv_python-4.12.0.88-cp37-abi3-win_amd64.whl.metadata (19 kB)
Requirement already satisfied: pillow>=7.1.2 in c:\users\lihen\anaconda3\lib\site-packages (from ultralytics==8.3.234) (11.1.0)
Requirement already satisfied: pyyaml>=5.3.1 in c:\users\lihen\anaconda3\lib\site-packages (from ultralytics==8.3.234) (6.0.2)
Requirement already satisfied: requests>=2.23.0 in c:\users\lihen\anaconda3\lib\site-packages (from ultralytics==8.3.234) (2.32.3)
Requirement already satisfied: scipy>=1.4.1 in c:\users\lihen\anaconda3\lib\site-packages (from ultralytics==8.3.234) (1.15.3)
Collecting torch>=1.8.0 (from ultralytics==8.3.234)
Downloading torch-2.9.1-cp313-cp313-win_amd64.whl.metadata (30 kB)
Collecting torchvision>=0.9.0 (from ultralytics==8.3.234)
Downloading torchvision-0.24.1-cp313-cp313-win_amd64.whl.metadata (5.9 kB)
Requirement already satisfied: psutil>=5.8.0 in c:\users\lihen\anaconda3\lib\site-packages (from ultralytics==8.3.234) (5.9.0)
Collecting polars>=0.20.0 (from ultralytics==8.3.234)
Downloading polars-1.35.2-py3-none-any.whl.metadata (10 kB)
Collecting ultralytics-thop>=2.0.18 (from ultralytics==8.3.234)
Downloading ultralytics_thop-2.0.18-py3-none-any.whl.metadata (14 kB)
Requirement already satisfied: contourpy>=1.0.1 in c:\users\lihen\anaconda3\lib\site-packages (from matplotlib>=3.3.0->ultralytics==8.3.234) (1.3.1)
Requirement already satisfied: cycler>=0.10 in c:\users\lihen\anaconda3\lib\site-packages (from matplotlib>=3.3.0->ultralytics==8.3.234) (0.11.0)
Requirement already satisfied: fonttools>=4.22.0 in c:\users\lihen\anaconda3\lib\site-packages (from matplotlib>=3.3.0->ultralytics==8.3.234) (4.55.3)
Requirement already satisfied: kiwisolver>=1.3.1 in c:\users\lihen\anaconda3\lib\site-packages (from matplotlib>=3.3.0->ultralytics==8.3.234) (1.4.8)
Requirement already satisfied: packaging>=20.0 in c:\users\lihen\anaconda3\lib\site-packages (from matplotlib>=3.3.0->ultralytics==8.3.234) (24.2)
Requirement already satisfied: pyparsing>=2.3.1 in c:\users\lihen\anaconda3\lib\site-packages (from matplotlib>=3.3.0->ultralytics==8.3.234) (3.2.0)
Requirement already satisfied: python-dateutil>=2.7 in c:\users\lihen\anaconda3\lib\site-packages (from matplotlib>=3.3.0->ultralytics==8.3.234) (2.9.0.post0)
Collecting polars-runtime-32==1.35.2 (from polars>=0.20.0->ultralytics==8.3.234)
Downloading polars_runtime_32-1.35.2-cp39-abi3-win_amd64.whl.metadata (1.5 kB)
Requirement already satisfied: six>=1.5 in c:\users\lihen\anaconda3\lib\site-packages (from python-dateutil>=2.7->matplotlib>=3.3.0->ultralytics==8.3.234) (1.17.0)
Requirement already satisfied: charset-normalizer<4,>=2 in c:\users\lihen\anaconda3\lib\site-packages (from requests>=2.23.0->ultralytics==8.3.234) (3.3.2)
Requirement already satisfied: idna<4,>=2.5 in c:\users\lihen\anaconda3\lib\site-packages (from requests>=2.23.0->ultralytics==8.3.234) (3.7)
Requirement already satisfied: urllib3<3,>=1.21.1 in c:\users\lihen\anaconda3\lib\site-packages (from requests>=2.23.0->ultralytics==8.3.234) (2.3.0)
Requirement already satisfied: certifi>=2017.4.17 in c:\users\lihen\anaconda3\lib\site-packages (from requests>=2.23.0->ultralytics==8.3.234) (2025.4.26)
Requirement already satisfied: filelock in c:\users\lihen\anaconda3\lib\site-packages (from torch>=1.8.0->ultralytics==8.3.234) (3.17.0)
Requirement already satisfied: typing-extensions>=4.10.0 in c:\users\lihen\anaconda3\lib\site-packages (from torch>=1.8.0->ultralytics==8.3.234) (4.12.2)
Requirement already satisfied: sympy>=1.13.3 in c:\users\lihen\anaconda3\lib\site-packages (from torch>=1.8.0->ultralytics==8.3.234) (1.13.3)
Requirement already satisfied: networkx>=2.5.1 in c:\users\lihen\anaconda3\lib\site-packages (from torch>=1.8.0->ultralytics==8.3.234) (3.4.2)
Requirement already satisfied: jinja2 in c:\users\lihen\anaconda3\lib\site-packages (from torch>=1.8.0->ultralytics==8.3.234) (3.1.6)
Requirement already satisfied: fsspec>=0.8.5 in c:\users\lihen\anaconda3\lib\site-packages (from torch>=1.8.0->ultralytics==8.3.234) (2025.3.2)
Requirement already satisfied: setuptools in c:\users\lihen\anaconda3\lib\site-packages (from torch>=1.8.0->ultralytics==8.3.234) (72.1.0)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in c:\users\lihen\anaconda3\lib\site-packages (from sympy>=1.13.3->torch>=1.8.0->ultralytics==8.3.234) (1.3.0)
Requirement already satisfied: MarkupSafe>=2.0 in c:\users\lihen\anaconda3\lib\site-packages (from jinja2->torch>=1.8.0->ultralytics==8.3.234) (3.0.2)
Downloading opencv_python-4.12.0.88-cp37-abi3-win_amd64.whl (39.0 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 39.0/39.0 MB 3.4 MB/s eta 0:00:00
Downloading polars-1.35.2-py3-none-any.whl (783 kB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 783.6/783.6 kB 8.7 MB/s eta 0:00:00
Downloading polars_runtime_32-1.35.2-cp39-abi3-win_amd64.whl (41.3 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 41.3/41.3 MB 3.1 MB/s eta 0:00:00
Downloading torch-2.9.1-cp313-cp313-win_amd64.whl (110.9 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 110.9/110.9 MB 3.1 MB/s eta 0:00:00
Downloading torchvision-0.24.1-cp313-cp313-win_amd64.whl (4.3 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.3/4.3 MB 3.9 MB/s eta 0:00:00
Downloading ultralytics_thop-2.0.18-py3-none-any.whl (28 kB)
Building wheels for collected packages: ultralytics
Building editable for ultralytics (pyproject.toml) ... done
Created wheel for ultralytics: filename=ultralytics-8.3.234-0.editable-py3-none-any.whl size=23392 sha256=a4d1ab7f57eee6a5ba0e1ceceb68d61317128342b3d384f25ea6329034a5748b
Stored in directory: C:\Users\lihen\AppData\Local\Temp\pip-ephem-wheel-cache-doqumx1m\wheels\32\6e\ca\222bde60b06772596cb47a005202e627db6a0c055016941066
Successfully built ultralytics
Installing collected packages: polars-runtime-32, opencv-python, torch, polars, ultralytics-thop, torchvision, ultralytics
Successfully installed opencv-python-4.12.0.88 polars-1.35.2 polars-runtime-32-1.35.2 torch-2.9.1 torchvision-0.24.1 ultralytics-8.3.234 ultralytics-thop-2.0.18

## Install onnx

(base) C:\HeLHDev\ultralytics>pip install onnx
Collecting onnx
Downloading onnx-1.20.0-cp312-abi3-win_amd64.whl.metadata (8.6 kB)
Requirement already satisfied: numpy>=1.23.2 in c:\users\lihen\anaconda3\lib\site-packages (from onnx) (2.1.3)
Requirement already satisfied: protobuf>=4.25.1 in c:\users\lihen\anaconda3\lib\site-packages (from onnx) (5.29.3)
Requirement already satisfied: typing_extensions>=4.7.1 in c:\users\lihen\anaconda3\lib\site-packages (from onnx) (4.12.2)
Collecting ml_dtypes>=0.5.0 (from onnx)
Downloading ml_dtypes-0.5.4-cp313-cp313-win_amd64.whl.metadata (9.2 kB)
Downloading onnx-1.20.0-cp312-abi3-win_amd64.whl (16.5 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.5/16.5 MB 4.0 MB/s eta 0:00:00
Downloading ml_dtypes-0.5.4-cp313-cp313-win_amd64.whl (212 kB)
Installing collected packages: ml_dtypes, onnx
Successfully installed ml_dtypes-0.5.4 onnx-1.20.0

## Install Pytorch

(base) C:\HeLHDev\ultralytics>pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
Looking in indexes: https://download.pytorch.org/whl/cu124
Requirement already satisfied: torch in c:\users\lihen\anaconda3\lib\site-packages (2.9.1)
Requirement already satisfied: torchvision in c:\users\lihen\anaconda3\lib\site-packages (0.24.1)
Collecting torchaudio
Downloading https://download.pytorch.org/whl/cu124/torchaudio-2.6.0%2Bcu124-cp313-cp313-win_amd64.whl.metadata (6.8 kB)
Requirement already satisfied: filelock in c:\users\lihen\anaconda3\lib\site-packages (from torch) (3.17.0)
Requirement already satisfied: typing-extensions>=4.10.0 in c:\users\lihen\anaconda3\lib\site-packages (from torch) (4.12.2)
Requirement already satisfied: sympy>=1.13.3 in c:\users\lihen\anaconda3\lib\site-packages (from torch) (1.13.3)
Requirement already satisfied: networkx>=2.5.1 in c:\users\lihen\anaconda3\lib\site-packages (from torch) (3.4.2)
Requirement already satisfied: jinja2 in c:\users\lihen\anaconda3\lib\site-packages (from torch) (3.1.6)
Requirement already satisfied: fsspec>=0.8.5 in c:\users\lihen\anaconda3\lib\site-packages (from torch) (2025.3.2)
Requirement already satisfied: setuptools in c:\users\lihen\anaconda3\lib\site-packages (from torch) (72.1.0)
Requirement already satisfied: numpy in c:\users\lihen\anaconda3\lib\site-packages (from torchvision) (2.1.3)
Requirement already satisfied: pillow!=8.3.\*,>=5.3.0 in c:\users\lihen\anaconda3\lib\site-packages (from torchvision) (11.1.0)
INFO: pip is looking at multiple versions of torchaudio to determine which version is compatible with other requirements. This could take a while.
Collecting torchvision
Downloading https://download.pytorch.org/whl/cu124/torchvision-0.21.0%2Bcu124-cp313-cp313-win_amd64.whl.metadata (6.3 kB)
Collecting torch
Downloading https://download.pytorch.org/whl/cu124/torch-2.6.0%2Bcu124-cp313-cp313-win_amd64.whl.metadata (28 kB)
Collecting sympy==1.13.1 (from torch)
Downloading https://download.pytorch.org/whl/sympy-1.13.1-py3-none-any.whl (6.2 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.2/6.2 MB 6.8 MB/s eta 0:00:00
Requirement already satisfied: mpmath<1.4,>=1.1.0 in c:\users\lihen\anaconda3\lib\site-packages (from sympy==1.13.1->torch) (1.3.0)
Requirement already satisfied: MarkupSafe>=2.0 in c:\users\lihen\anaconda3\lib\site-packages (from jinja2->torch) (3.0.2)
Downloading https://download.pytorch.org/whl/cu124/torchvision-0.21.0%2Bcu124-cp313-cp313-win_amd64.whl (6.1 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.1/6.1 MB 3.4 MB/s eta 0:00:00
Downloading https://download.pytorch.org/whl/cu124/torch-2.6.0%2Bcu124-cp313-cp313-win_amd64.whl (2532.3 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.5/2.5 GB 2.4 MB/s eta 0:00:00
Downloading https://download.pytorch.org/whl/cu124/torchaudio-2.6.0%2Bcu124-cp313-cp313-win_amd64.whl (4.2 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.2/4.2 MB 12.3 MB/s eta 0:00:00
Installing collected packages: sympy, torch, torchvision, torchaudio
Attempting uninstall: sympy
Found existing installation: sympy 1.13.3
Uninstalling sympy-1.13.3:
Successfully uninstalled sympy-1.13.3
Attempting uninstall: torch
Found existing installation: torch 2.9.1
Uninstalling torch-2.9.1:
Successfully uninstalled torch-2.9.1
Attempting uninstall: torchvision
Found existing installation: torchvision 0.24.1
Uninstalling torchvision-0.24.1:
Successfully uninstalled torchvision-0.24.1
Successfully installed sympy-1.13.1 torch-2.6.0+cu124 torchaudio-2.6.0+cu124 torchvision-0.21.0+cu124

## Install shapely

(base) C:\HeLHDev\ultralytics>pip install shapely
Collecting shapely
Downloading shapely-2.1.2-cp313-cp313-win_amd64.whl.metadata (7.1 kB)
Requirement already satisfied: numpy>=1.21 in c:\users\lihen\anaconda3\lib\site-packages (from shapely) (2.1.3)
Downloading shapely-2.1.2-cp313-cp313-win_amd64.whl (1.7 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 13.6 MB/s eta 0:00:00
Installing collected packages: shapely
Successfully installed shapely-2.1.2
