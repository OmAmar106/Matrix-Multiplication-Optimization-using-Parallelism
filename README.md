# Matrix Multiplication Optimization using Parallelism

## 📋 Overview

This project explores the optimization of **matrix multiplication** using **parallel computing** techniques such as **multithreading**. Traditional matrix multiplication has a time complexity of **O(n³)**, which becomes infeasible for large matrices. Our goal is to reduce this complexity theoretically to **O(n²)** by leveraging **multi-core processing** capabilities.

Inspired by **Square Root Decomposition**, our approach divides a large matrix into smaller blocks of size √n × √n and assigns independent threads to process each block, enabling simultaneous execution and optimized computation time.

## 🔍 Problem Statement

Traditional matrix multiplication is computationally intensive due to its cubic time complexity. This project presents a theoretical approach to parallelize the multiplication process using threads, aiming to:

- Divide the matrix into √n × √n blocks.
- Run n threads in parallel, each handling a block.
- Achieve a theoretical time complexity of **O(n²)**.

## 📈 Key Results

- For **small matrices**, multithreading introduces overhead and performs worse than traditional methods.
- For **larger matrices**, using threads up to the number of physical CPU cores results in faster performance.
- **Optimal performance** is achieved when the number of threads ≤ number of CPU cores.

## 🧪 Experimental Observations

- Performance improves as the number of threads increases — up to min of the number of available cores and root of the length of matrix.
- Beyond that, thread creation overhead dominates and reduces performance gains.
- A comparison between traditional and parallel methods (via graphs and tables) is provided in the report.

## 📈 Performance Summary

| Threads | Total Time (s) | Avg Time (per matrix) |
| ------- | -------------- | --------------------- |
| 4       | 1.9033         | 0.0202                |
| 9       | 2.0024         | 0.0213                |
| 16      | 2.0959         | 0.0222                |
| 25      | 2.2153         | 0.0235                |
| n       | 2.5013         | 0.0266                |

## 📚 References

- CUDA-based optimization strategies: [IEEE Link 1](https://ieeexplore.ieee.org/document/9935904)
- Multithreading analysis: [IEEE Link 2](https://ieeexplore.ieee.org/document/7972402)
