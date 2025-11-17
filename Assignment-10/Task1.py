import time
from typing import List

def find_common_messy(a: List, b: List) -> List:
    res = []
    for i in a:
        for j in b:
            if i == j:
                res.append(i)
    return res

def find_common_set_intersection(a: List, b: List) -> List:
    return list(set(a) & set(b))

def find_common_set_intersection_ordered(a: List, b: List) -> List:
    return [x for x in a if x in set(b)]

def find_common_filter(a: List, b: List) -> List:
    b_set = set(b)
    return list(filter(lambda x: x in b_set, a))

def find_common_comprehension(a: List, b: List) -> List:
    b_set = set(b)
    return [x for x in a if x in b_set]

def benchmark_functions(a: List, b: List, num_runs: int = 1000):
    functions = [
        ("Messy (Nested Loop)", find_common_messy),
        ("Set Intersection", find_common_set_intersection),
        ("Set Intersection (Ordered)", find_common_set_intersection_ordered),
        ("Filter with Set", find_common_filter),
        ("List Comprehension", find_common_comprehension),
    ]
    
    print("=" * 80)
    print("LOOP OPTIMIZATION BENCHMARK")
    print("=" * 80)
    print(f"Input: list_a (length {len(a)}), list_b (length {len(b)})")
    print(f"Benchmark runs: {num_runs} iterations\n")
    
    results = {}
    
    for name, func in functions:
        start_time = time.perf_counter()
        for _ in range(num_runs):
            result = func(a, b)
        end_time = time.perf_counter()
        
        elapsed = (end_time - start_time) * 1000
        results[name] = elapsed
        
        print(f"{name:.<40} {elapsed:>10.4f} ms")
    
    print("\n" + "=" * 80)
    print("OPTIMIZATION ANALYSIS")
    print("=" * 80)
    
    baseline = results["Messy (Nested Loop)"]
    for name, time_taken in results.items():
        speedup = baseline / time_taken
        improvement = ((baseline - time_taken) / baseline) * 100
        print(f"{name:.<40} {speedup:>6.2f}x faster, {improvement:>6.1f}% improvement")

def demonstrate_correctness():
    print("\n" + "=" * 80)
    print("CORRECTNESS VERIFICATION")
    print("=" * 80)
    
    test_cases = [
        ([1, 2, 3, 4, 5], [3, 4, 5, 6, 7], "Basic overlapping lists"),
        ([1, 2, 3], [4, 5, 6], "No common elements"),
        ([1, 1, 2, 2, 3], [1, 2, 3], "Duplicates in first list"),
        ([1, 2, 3], [1, 1, 2, 2, 3], "Duplicates in second list"),
        ([], [1, 2, 3], "Empty first list"),
        ([1, 2, 3], [], "Empty second list"),
        ([], [], "Both empty"),
        ([5], [5], "Single common element"),
        (list(range(100)), list(range(50, 150)), "Large lists with overlap"),
    ]
    
    print(f"{'Test Case':<50} {'Result':<20}")
    print("-" * 70)
    
    for a, b, description in test_cases:
        result_messy = set(find_common_messy(a, b))
        result_set = set(find_common_set_intersection(a, b))
        result_comp = set(find_common_comprehension(a, b))
        
        match = (result_messy == result_set == result_comp)
        status = "✓ PASS" if match else "✗ FAIL"
        
        print(f"{description:<50} {status:<20}")

def demonstrate_code_quality():
    print("\n" + "=" * 80)
    print("CODE QUALITY COMPARISON")
    print("=" * 80)
    
    comparison = {
        "Messy (Nested Loop)": {
            "time_complexity": "O(n × m)",
            "space_complexity": "O(k)",
            "readability": "Poor",
            "pythonic": "No",
            "lines_of_code": 4,
        },
        "Set Intersection": {
            "time_complexity": "O(n + m)",
            "space_complexity": "O(n + m)",
            "readability": "Excellent",
            "pythonic": "Yes",
            "lines_of_code": 1,
        },
        "List Comprehension": {
            "time_complexity": "O(n + m)",
            "space_complexity": "O(k)",
            "readability": "Very Good",
            "pythonic": "Yes",
            "lines_of_code": 2,
        },
    }
    
    print(f"{'Approach':<25} {'Time':<15} {'Space':<15} {'Readable':<15} {'Pythonic':<12}")
    print("-" * 82)
    
    for approach, metrics in comparison.items():
        print(f"{approach:<25} {metrics['time_complexity']:<15} {metrics['space_complexity']:<15} {metrics['readability']:<15} {metrics['pythonic']:<12}")

def main():
    small_list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    small_list_b = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    
    print("EXAMPLE: Find common elements between two lists")
    print(f"List A: {small_list_a}")
    print(f"List B: {small_list_b}")
    print()
    
    print("Messy version result:", find_common_messy(small_list_a, small_list_b))
    print("Optimized version result:", find_common_set_intersection(small_list_a, small_list_b))
    print()
    
    medium_list_a = list(range(500))
    medium_list_b = list(range(250, 750))
    
    benchmark_functions(medium_list_a, medium_list_b, num_runs=1000)
    
    demonstrate_correctness()
    
    demonstrate_code_quality()
    
    print("\n" + "=" * 80)
    print("KEY OPTIMIZATION INSIGHTS")
    print("=" * 80)
    print("1. Nested loops: O(n × m) complexity - avoid for large datasets")
    print("2. Set intersection: O(n + m) complexity - much faster")
    print("3. List comprehension with set: O(n + m) - preserves order, very Pythonic")
    print("4. Set operations lose ordering - use comprehension if order matters")
    print("5. For small lists, differences are negligible")
    print("6. For large lists, optimization is critical")
    print("=" * 80)

if __name__ == "__main__":
    main()
