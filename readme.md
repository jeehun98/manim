# Manim 초기 환경 설정 가이드 (Windows, venv 기준)

## 1. 가상환경 생성 및 활성화
```ps
# 프로젝트 폴더로 이동
cd C:\Users\as042\OneDrive\Desktop\manim\manim

# 가상환경 생성
python -m venv .venv

# 가상환경 활성화 (PowerShell)
. .\.venv\Scripts\Activate.ps1
```

---

## 2. Manim 설치
```ps
pip install manim
```

---

## 3. 필수 외부 프로그램 설치

### (1) LaTeX (수식 렌더링용)
- **MiKTeX 다운로드:** [https://miktex.org/download](https://miktex.org/download)  
- 설치 시 **“Install missing packages on-the-fly: Yes”** 선택
- 확인:
  ```ps
  latex --version
  dvisvgm --version
  ```

### (2) Ghostscript (dvisvgm 보조용)
- **Ghostscript 다운로드:** [https://ghostscript.com/releases/gsdnld.html](https://ghostscript.com/releases/gsdnld.html)
- 확인:
  ```ps
  gswin64c --version
  ```

### (3) FFmpeg (영상/오디오 인코딩)
```ps
winget install --id=Gyan.FFmpeg -e
```
- 확인:
  ```ps
  ffmpeg -version
  ```

---

## 4. PATH 설정 (venv에서 인식 안 될 경우)

`Activate.ps1` 마지막 줄에 추가:
```ps
# .venv\Scripts\Activate.ps1
$env:Path = "C:\Program Files\MiKTeX\miktex\bin\x64;C:\Program Files\gs\gs10.04.0\bin;C:\Program Files\FFmpeg\bin;" + $env:Path
```

이후 venv 활성화 시 자동 적용.

---

## 5. 테스트 실행

### (1) LaTeX 사용
```python
from manim import *

class HelloManim(Scene):
    def construct(self):
        t = Tex(r"Hello, \\texttt{Manim}!")
        self.play(Write(t))
        self.wait(0.5)
        self.play(t.animate.set_color(YELLOW).scale(1.2))
        self.wait()
```

실행:
```ps
manim -pqh manim_quickstart.py HelloManim
```

### (2) LaTeX 없이 텍스트만 (간단 확인)
```python
from manim import *

class HelloManim(Scene):
    def construct(self):
        t = Text("Hello, Manim!")
        self.play(Write(t))
        self.wait()
```

---

## 6. 문제 발생 시 체크리스트
- `where latex` / `where dvisvgm` / `where gswin64c` / `where ffmpeg` → 실행 파일 경로 확인  
- `latex` 실행 시 패키지 자동 설치 프롬프트 나오면 **Install** 선택  
- `Tex` 대신 `Text/MarkupText` 쓰면 LaTeX 설치 없어도 사용 가능  
