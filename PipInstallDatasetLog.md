
(base) C:\Users\lihen>conda env list

# conda environments:
#
base                 * C:\Users\lihen\anaconda3


(base) C:\Users\lihen>python
Python 3.13.5 | packaged by Anaconda, Inc. | (main, Jun 12 2025, 16:37:03) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()

(base) C:\Users\lihen>pip install datasets
Collecting datasets
  Downloading datasets-4.4.1-py3-none-any.whl.metadata (19 kB)
Requirement already satisfied: filelock in c:\users\lihen\anaconda3\lib\site-packages (from datasets) (3.17.0)
Requirement already satisfied: numpy>=1.17 in c:\users\lihen\anaconda3\lib\site-packages (from datasets) (2.1.3)
Collecting pyarrow>=21.0.0 (from datasets)
  Downloading pyarrow-22.0.0-cp313-cp313-win_amd64.whl.metadata (3.3 kB)
Requirement already satisfied: dill<0.4.1,>=0.3.0 in c:\users\lihen\anaconda3\lib\site-packages (from datasets) (0.3.8)
Requirement already satisfied: pandas in c:\users\lihen\anaconda3\lib\site-packages (from datasets) (2.2.3)
Requirement already satisfied: requests>=2.32.2 in c:\users\lihen\anaconda3\lib\site-packages (from datasets) (2.32.3)
Requirement already satisfied: httpx<1.0.0 in c:\users\lihen\anaconda3\lib\site-packages (from datasets) (0.28.1)
Requirement already satisfied: tqdm>=4.66.3 in c:\users\lihen\anaconda3\lib\site-packages (from datasets) (4.67.1)
Collecting xxhash (from datasets)
  Downloading xxhash-3.6.0-cp313-cp313-win_amd64.whl.metadata (13 kB)
Collecting multiprocess<0.70.19 (from datasets)
  Downloading multiprocess-0.70.18-py313-none-any.whl.metadata (7.2 kB)
Requirement already satisfied: fsspec<=2025.10.0,>=2023.1.0 in c:\users\lihen\anaconda3\lib\site-packages (from fsspec[http]<=2025.10.0,>=2023.1.0->datasets) (2025.3.2)
Collecting huggingface-hub<2.0,>=0.25.0 (from datasets)
  Downloading huggingface_hub-1.1.7-py3-none-any.whl.metadata (13 kB)
Requirement already satisfied: packaging in c:\users\lihen\anaconda3\lib\site-packages (from datasets) (24.2)
Requirement already satisfied: pyyaml>=5.1 in c:\users\lihen\anaconda3\lib\site-packages (from datasets) (6.0.2)
Requirement already satisfied: aiohttp!=4.0.0a0,!=4.0.0a1 in c:\users\lihen\anaconda3\lib\site-packages (from fsspec[http]<=2025.10.0,>=2023.1.0->datasets) (3.11.10)
Requirement already satisfied: anyio in c:\users\lihen\anaconda3\lib\site-packages (from httpx<1.0.0->datasets) (4.7.0)
Requirement already satisfied: certifi in c:\users\lihen\anaconda3\lib\site-packages (from httpx<1.0.0->datasets) (2025.4.26)
Requirement already satisfied: httpcore==1.* in c:\users\lihen\anaconda3\lib\site-packages (from httpx<1.0.0->datasets) (1.0.9)
Requirement already satisfied: idna in c:\users\lihen\anaconda3\lib\site-packages (from httpx<1.0.0->datasets) (3.7)
Requirement already satisfied: h11>=0.16 in c:\users\lihen\anaconda3\lib\site-packages (from httpcore==1.*->httpx<1.0.0->datasets) (0.16.0)
Collecting hf-xet<2.0.0,>=1.2.0 (from huggingface-hub<2.0,>=0.25.0->datasets)
  Downloading hf_xet-1.2.0-cp37-abi3-win_amd64.whl.metadata (5.0 kB)
Requirement already satisfied: shellingham in c:\users\lihen\anaconda3\lib\site-packages (from huggingface-hub<2.0,>=0.25.0->datasets) (1.5.0)
Collecting typer-slim (from huggingface-hub<2.0,>=0.25.0->datasets)
  Downloading typer_slim-0.20.0-py3-none-any.whl.metadata (16 kB)
Requirement already satisfied: typing-extensions>=3.7.4.3 in c:\users\lihen\anaconda3\lib\site-packages (from huggingface-hub<2.0,>=0.25.0->datasets) (4.12.2)
Collecting dill<0.4.1,>=0.3.0 (from datasets)
  Downloading dill-0.4.0-py3-none-any.whl.metadata (10 kB)
Requirement already satisfied: aiohappyeyeballs>=2.3.0 in c:\users\lihen\anaconda3\lib\site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.10.0,>=2023.1.0->datasets) (2.4.4)
Requirement already satisfied: aiosignal>=1.1.2 in c:\users\lihen\anaconda3\lib\site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.10.0,>=2023.1.0->datasets) (1.2.0)
Requirement already satisfied: attrs>=17.3.0 in c:\users\lihen\anaconda3\lib\site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.10.0,>=2023.1.0->datasets) (24.3.0)
Requirement already satisfied: frozenlist>=1.1.1 in c:\users\lihen\anaconda3\lib\site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.10.0,>=2023.1.0->datasets) (1.5.0)
Requirement already satisfied: multidict<7.0,>=4.5 in c:\users\lihen\anaconda3\lib\site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.10.0,>=2023.1.0->datasets) (6.1.0)
Requirement already satisfied: propcache>=0.2.0 in c:\users\lihen\anaconda3\lib\site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.10.0,>=2023.1.0->datasets) (0.3.1)
Requirement already satisfied: yarl<2.0,>=1.17.0 in c:\users\lihen\anaconda3\lib\site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.10.0,>=2023.1.0->datasets) (1.18.0)
Requirement already satisfied: charset-normalizer<4,>=2 in c:\users\lihen\anaconda3\lib\site-packages (from requests>=2.32.2->datasets) (3.3.2)
Requirement already satisfied: urllib3<3,>=1.21.1 in c:\users\lihen\anaconda3\lib\site-packages (from requests>=2.32.2->datasets) (2.3.0)
Requirement already satisfied: colorama in c:\users\lihen\anaconda3\lib\site-packages (from tqdm>=4.66.3->datasets) (0.4.6)
Requirement already satisfied: sniffio>=1.1 in c:\users\lihen\anaconda3\lib\site-packages (from anyio->httpx<1.0.0->datasets) (1.3.0)
Requirement already satisfied: python-dateutil>=2.8.2 in c:\users\lihen\anaconda3\lib\site-packages (from pandas->datasets) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in c:\users\lihen\anaconda3\lib\site-packages (from pandas->datasets) (2024.1)
Requirement already satisfied: tzdata>=2022.7 in c:\users\lihen\anaconda3\lib\site-packages (from pandas->datasets) (2025.2)
Requirement already satisfied: six>=1.5 in c:\users\lihen\anaconda3\lib\site-packages (from python-dateutil>=2.8.2->pandas->datasets) (1.17.0)
Requirement already satisfied: click>=8.0.0 in c:\users\lihen\anaconda3\lib\site-packages (from typer-slim->huggingface-hub<2.0,>=0.25.0->datasets) (8.1.8)
Downloading datasets-4.4.1-py3-none-any.whl (511 kB)
Downloading huggingface_hub-1.1.7-py3-none-any.whl (516 kB)
Downloading hf_xet-1.2.0-cp37-abi3-win_amd64.whl (2.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.9/2.9 MB 22.4 MB/s eta 0:00:00
Downloading multiprocess-0.70.18-py313-none-any.whl (151 kB)
Downloading dill-0.4.0-py3-none-any.whl (119 kB)
Downloading pyarrow-22.0.0-cp313-cp313-win_amd64.whl (28.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 28.0/28.0 MB 3.3 MB/s eta 0:00:00
Downloading typer_slim-0.20.0-py3-none-any.whl (47 kB)
Downloading xxhash-3.6.0-cp313-cp313-win_amd64.whl (31 kB)
Installing collected packages: xxhash, pyarrow, hf-xet, dill, typer-slim, multiprocess, huggingface-hub, datasets
  Attempting uninstall: pyarrow
    Found existing installation: pyarrow 19.0.0
    Uninstalling pyarrow-19.0.0:
      Successfully uninstalled pyarrow-19.0.0
  Attempting uninstall: dill
    Found existing installation: dill 0.3.8
    Uninstalling dill-0.3.8:
      Successfully uninstalled dill-0.3.8
Successfully installed datasets-4.4.1 dill-0.4.0 hf-xet-1.2.0 huggingface-hub-1.1.7 multiprocess-0.70.18 pyarrow-22.0.0 typer-slim-0.20.0 xxhash-3.6.0