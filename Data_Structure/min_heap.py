from typing import Generic, TypeVar, NoReturn, List, Optional
from utils.comparison import Comparison

T = TypeVar("T")

class Node(Generic[T]) :
    def __init__(self, data : T, sort_index : int) -> NoReturn :
        self.data = data
        self.sort_index = sort_index

class MinHeap(Generic[T]) :
    def __init__(self, heap : List[Node[T]] = []) -> NoReturn :
        self.heap = heap

    @staticmethod
    def _compare(a : Node[T], b : Node[T]) -> Optional[Comparison] :
        diff = a.sort_index - b.sort_index

        if diff == 0 :
            try :
                if a.data < b.data :
                    return Comparison.Less
                elif a.data == b.data :
                    return Comparison.Equal
                else :
                    return Comparison.Greater
            except TypeError as error :
                print("[Type Error]: The data of nodes cannot be compared.")
                return None
        elif diff < 0 :
            return Comparison.Less
        else :
            return Comparison.Greater

    def peek(self) -> Optional[Node[T]] :
        """
        This method returns the minimal node of the min-heap.
        """
        if len(self.heap) == 0 :
            return None
        else :
            return self.heap[0]

    def sift_up(self, node : T, i : int) -> NoReturn :
        """
        This method sifts the node up.

        Args:
            node: The node to be sifted up.
            i: The index of `node`.
        """
        index = i
        while index > 0 :
            parent_index = (i - 1) >> 1
            parent = self.heap[parent_index]

            match MinHeap._compare(parent, node) :
                case Comparison.Greater :
                    heap[parent_index] = node
                    heap[index] = parent
                    index = parent_index
                    break;
                case Comparison.Equal :
                    return;
                case Comparison.Less :
                    return;

    def sift_down(self, node : T, i : int) -> NoReturn :
        """
        This method sifts the node down.

        Args:
            node: The node to be sifted down.
            i: The index of `node`.
        """
        index = i
        length = len(self.heap)
        half_length = length >> 1

        # Only process nodes that have at least one child (up to last non-leaf node)
        # Half length is the index of last child which has at least one child

        while index < half_length :
            left_index = (index + 1) * 2 - 1
            left = self.heap[left_index]
            right_index = left_index + 1
            right = self.heap[right_index]

            if MinHeap._compare(left, node) == Comparison.Less :
                # Left child is smaller

                if right_index < length and \
                    MinHeap._compare(right, left) == Comparison.Less :
                    # Right child is smaller than left, swap the right

                    self.heap[index] = right
                    self.heap[right_index] = node
                    index = right_index
                else :
                    # Left child is smallest, swap with left

                    self.heap[index] = left
                    self.heap[left_index] = node
                    index = left_index
            elif right_index < length and MinHeap._compare(right, node) == Comparison.Less :
                # Left child doesn't exist and only right child exists

                self.heap[index] = right
                self.heap[right_index] = node
                index = right_index

    def push(self, node : T) -> NoReturn :
        """
        This method pushes a new node to the binary tree.
        """

        index = len(self.heap)
        self.heap.append(node)
        self.sift_up(node, index)

    def pop(self) -> Optional[Node[T]] :
        """
        This method pops the minimal node of the min-heap.
        """

        if len(self.heap) == 0 :
            return None

        first = self.heap[0]
        last = self.heap.pop()

        if last != first :
            self.heap[0] = last
            self.sift_down(last, 0)

        return first