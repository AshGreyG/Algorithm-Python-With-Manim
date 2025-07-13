from utils.simp_benchmark import function_timer
from .bubble_sort import bubble_sort, memorized_bubble_sort
from typing import List, NoReturn, TypeVar, Tuple, Callable

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = "/usr/share/fonts/libertinus/LibertinusSerif-Regular.ttf"
libertinus_font = fm.FontProperties(fname = font_path)

plt.figure(figsize = (6, 6))

T = TypeVar("T")
Func = TypeVar("Func", bound = Callable[List[T], NoReturn])

ONE_ROUND_TIMES = 100
GEN_MINIMAL = 20
GEN_MAXIMAL = 100
BENCH_MINIMAL = 200
BENCH_MAXIMAL = 450
BENCH_STEP = 5
FAST_COMPLEXITY_SCALE = 150

@function_timer
def single_benchmark(array : List[T], func : Func) :
    func(array)

def dynamic_benchmark(func : Func) -> NoReturn :
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
        for i in range(0, ONE_ROUND_TIMES) :
            arr = np.random.randint(
                GEN_MINIMAL,
                GEN_MAXIMAL,
                size = size
            ).tolist()
            average_bench_res.append(single_benchmark(arr, func))

        best_bench_res : List[float] = []
        for i in range(0, ONE_ROUND_TIMES) :
            arr = sorted(np.random.randint(
                GEN_MINIMAL,
                GEN_MAXIMAL,
                size = size
            ).tolist())
            best_bench_res.append(single_benchmark(arr, func))

        worst_bench_res : List[float] = []
        for i in range(0, ONE_ROUND_TIMES) :
            arr = sorted(np.random.randint(
                GEN_MINIMAL,
                GEN_MAXIMAL,
                size = size
            ).tolist(), reverse = True)
            worst_bench_res.append(single_benchmark(arr, func))

        res.append((
            float(np.average(best_bench_res)),
            float(np.average(average_bench_res)),
            float(np.average(worst_bench_res))
        ))

    min_res = list(map(lambda x : x[0], res))
    avr_res = list(map(lambda x : x[1] / FAST_COMPLEXITY_SCALE, res))
    max_res = list(map(lambda x : x[2] / FAST_COMPLEXITY_SCALE, res))

    plt.fill_between(
        range(BENCH_MINIMAL, BENCH_MAXIMAL, BENCH_STEP),
        min_res,
        max_res,
        alpha = 0.3,
        linewidth = 0
    )
    plt.plot(
        range(BENCH_MINIMAL, BENCH_MAXIMAL, BENCH_STEP),
        avr_res,
        alpha = 0.6
    )
    plt.xlabel(
        "Array Size",
        fontproperties = libertinus_font,
        fontsize = 14
    )
    plt.ylabel(
        "Algorithm Execution Time (× 150 μs)",
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
    dynamic_benchmark(bubble_sort)
    dynamic_benchmark(memorized_bubble_sort)
    plt.savefig("Bubble-Sort-Benchmark.svg", format = "svg")
