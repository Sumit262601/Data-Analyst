"""
Broadcasting vs Vectorization in NumPy: Theoretical Overview
Vectorization

Vectorization is a programming concept that focuses on converting scalar operations into vector operations. It's fundamentally about:

Definition:

    Converting element-by-element operations into single array operations
    Eliminating explicit loops in code
    Moving iterations to the compiled layer rather than the interpreted layer
Key Characteristics:

    Operates on entire arrays simultaneously
    Improves computational efficiency
    Reduces code complexity
    Works with arrays of same dimensions
Purpose:

    Performance optimization
    Code simplification
    Memory efficiency

Broadcasting
Broadcasting is a mechanism that allows NumPy to perform operations on arrays of different shapes. It consists of:

Definition:

    A set of rules for performing operations on arrays with different dimensions
    Automatic expansion of smaller arrays to match the shape of larger arrays
    Virtual replication without actual memory copying
Key Rules:

    Arrays must have compatible shapes
    Dimensions are matched from right to left
    Either dimension must be 1 or both dimensions must be equal
Purpose:

    Enable operations between arrays of different shapes
    Maintain memory efficiency
    Simplify array operations without explicit expansion
    Key Distinctions
Primary Focus:

    Vectorization: Performance and optimization
    Broadcasting: Shape compatibility and operation flexibility
Memory Handling:

    Vectorization: Works with existing array memory
    Broadcasting: Creates virtual copies without actual memory allocation
Operation Type:

    Vectorization: Same operation across all elements
    Broadcasting: Shape-aware operations across different sized arrays
Implementation Level:

    Vectorization: Computation optimization
    Broadcasting: Array shape management
"""