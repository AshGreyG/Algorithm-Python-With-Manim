from .utils.simp_benchmark import (
    function_timer, 
    function_memory_monitor
)
from algorithm.sort.bubble_sort import (
    bubble_sort, 
    memorized_bubble_sort
)
from typing import (
    List, 
    TypeVar, 
    Tuple, 
    Callable
)
from .utils.color import (
    EverForestBackgroundColor,
    EverForestWarmColor,
    EverForestCoolColor
)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = "/usr/share/fonts/libertinus/LibertinusSerif-Regular.ttf"
libertinus_font = fm.FontProperties(fname = font_path)

plt.rcParams["figure.facecolor"] = EverForestBackgroundColor
plt.rcParams["axes.facecolor"] = EverForestBackgroundColor

T = TypeVar("T")

ONE_ROUND_TIMES = 100
GEN_MINIMAL = 20
GEN_MAXIMAL = 100
BENCH_MINIMAL = 200
BENCH_MAXIMAL = 450
BENCH_STEP = 5
TIME_COMPLEXITY_SCALE = 150
MEMO_COMPLEXITY_SCALE = 10000

NORMAL_COLOR = EverForestWarmColor[
    np.random.randint(0, len(EverForestWarmColor))
]
MEMORIZED_COLOR = EverForestCoolColor[
    np.random.randint(0, len(EverForestCoolColor))
]

@function_timer
def single_benchmark_time(array : List[T], func : Callable[..., None]) -> None :
    func(array)

# Notice, `single_benchmark_time` is an independent function and its return type
# is determined by itself not the decorator function.

def dynamic_benchmark_time(
    func : Callable[..., None], 
    color : str,
    fill_between_label : str,
    plot_label : str
) -> None :
    """
    This is the benchmark function for bubble sort / memorized bubble sort.

    Review:
        + Because the constant coefficient of best-case complexity is
            a tiny value (related to CPU cycle). If we draw worst and
            best together, the lower bound of chart seems to be a 
            constant complexity, so we set a y-scale (here set 150) for
            max-case and average-case complexity.
    """

    res : List[Tuple[float, float, float]] = []
    for size in range(BENCH_MINIMAL, BENCH_MAXIMAL, BENCH_STEP) :
        average_bench_res : List[float] = []
        for _ in range(0, ONE_ROUND_TIMES) :
            arr = np.random.randint(
                GEN_MINIMAL,
                GEN_MAXIMAL,
                size = size
            ).tolist()
            average_bench_res.append(single_benchmark_time(arr, func))

        best_bench_res : List[float] = []
        for _ in range(0, ONE_ROUND_TIMES) :
            arr = sorted(np.random.randint(
                GEN_MINIMAL,
                GEN_MAXIMAL,
                size = size
            ).tolist())
            best_bench_res.append(single_benchmark_time(arr, func))

        worst_bench_res : List[float] = []
        for _ in range(0, ONE_ROUND_TIMES) :
            arr = sorted(np.random.randint(
                GEN_MINIMAL,
                GEN_MAXIMAL,
                size = size
            ).tolist(), reverse = True)
            worst_bench_res.append(single_benchmark_time(arr, func))

        res.append((
            float(np.average(best_bench_res)),
            float(np.average(average_bench_res)),
            float(np.average(worst_bench_res))
        ))

    min_res = list(map(lambda x : x[0], res))
    avr_res = list(map(lambda x : x[1] / TIME_COMPLEXITY_SCALE, res))
    max_res = list(map(lambda x : x[2] / TIME_COMPLEXITY_SCALE, res))

    plt.fill_between(
        range(BENCH_MINIMAL, BENCH_MAXIMAL, BENCH_STEP),
        min_res,
        max_res,
        color = color,
        alpha = 0.3,
        linewidth = 0,
        label = fill_between_label
    )
    plt.plot(
        range(BENCH_MINIMAL, BENCH_MAXIMAL, BENCH_STEP),
        avr_res,
        color = color,
        alpha = 0.6,
        label = plot_label
    )
    plt.xlabel(
        "Array Size",
        fontproperties = libertinus_font,
        fontsize = 14
    )
    plt.ylabel(
        "Algorithm Execution Time (× 150 μs)",
        fontproperties = libertinus_font,
        fontsize = 15
    )
    plt.xticks(
        fontproperties = libertinus_font,
        fontsize = 12
    )
    plt.yticks(
        fontproperties = libertinus_font,
        fontsize = 12
    )

@function_memory_monitor()
def single_benchmark_memory(array : List[T], func : Callable[..., None]) -> None :
    func(array)

def dynamic_benchmark_memory(
    func : Callable[..., None], 
    color : str,
    fill_between_label : str,
    plot_label : str
) -> None :
    res : List[Tuple[float, float, float]] = []
    for size in range(BENCH_MINIMAL, BENCH_MAXIMAL, BENCH_STEP) :
        average_bench_res : List[float] = []
        for _ in range(0, ONE_ROUND_TIMES) :
            arr = np.random.randint(
                GEN_MINIMAL,
                GEN_MAXIMAL,
                size = size
            ).tolist()
            average_bench_res.append(single_benchmark_memory(arr, func))
        res.append((
            int(np.min(average_bench_res)),
            int(np.average(average_bench_res)),
            int(np.max(average_bench_res))
        ))

    min_res = list(map(lambda x : x[0], res))
    avr_res = list(map(lambda x : x[1] / MEMO_COMPLEXITY_SCALE, res))
    max_res = list(map(lambda x : x[2] / MEMO_COMPLEXITY_SCALE, res))

    plt.fill_between(
        range(BENCH_MINIMAL, BENCH_MAXIMAL, BENCH_STEP),
        min_res,
        max_res,
        color = color,
        alpha = 0.3,
        linewidth = 0,
        label = fill_between_label
    )
    plt.plot(
        range(BENCH_MINIMAL, BENCH_MAXIMAL, BENCH_STEP),
        avr_res,
        color = color,
        alpha = 0.6,
        label = plot_label
    )
    plt.xlabel(
        "Array Size",
        fontproperties = libertinus_font,
        fontsize = 14
    )
    plt.ylabel(
        "Algorithm Execution Memory (× 10⁴)",
        fontproperties = libertinus_font,
        fontsize = 14
    )
    plt.xticks(
        fontproperties = libertinus_font,
        fontsize = 12
    )
    plt.yticks(
        fontproperties = libertinus_font,
        fontsize = 12
    )

if __name__ == "__main__" :
    plt.figure(figsize = (6, 6))
    dynamic_benchmark_time(
        bubble_sort, 
        NORMAL_COLOR,
        "Normal-Range",
        "Normal-Average"
    )
    dynamic_benchmark_time(
        memorized_bubble_sort,
        MEMORIZED_COLOR,
        "Memorized-Range",
        "Memorized-Average"
    )
    plt.legend(loc = "upper left", prop = libertinus_font)
    plt.savefig("Bubble-Sort-Benchmark-Time.svg", format = "svg")

    plt.figure(figsize = (6, 6))
    dynamic_benchmark_memory(
        bubble_sort, 
        NORMAL_COLOR,
        "Normal-Range",
        "Normal-Average"
    )
    dynamic_benchmark_memory(
        memorized_bubble_sort, 
        MEMORIZED_COLOR,
        "Memorized-Range",
        "Memorized-Average"
    )
    plt.legend(loc = "upper left", prop = libertinus_font)
    plt.savefig("Bubble-Sort-Benchmark-Memory.svg", format = "svg")
