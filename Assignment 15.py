import gc
import tracemalloc

def create_objects():
    obj1 = [1, 2, 3, 4, 5]
    obj2 = {"a": 10, "b": 20}
    obj3 = "Hello Python"

    return obj1, obj2, obj3

def display_memory():
    current, peak = tracemalloc.get_traced_memory()
    print("Current Memory:", current)
    print("Peak Memory:", peak)

tracemalloc.start()

print("Initial Memory Usage:")
display_memory()

obj1, obj2, obj3 = create_objects()

print("\nMemory After Creating Objects:")
display_memory()

del obj1
del obj2
del obj3

gc.set_debug(gc.DEBUG_STATS)

print("\nGarbage Collection:")
gc.collect()

print("\nMemory After Garbage Collection:")
display_memory()

gc.set_debug(0)

tracemalloc.stop()
