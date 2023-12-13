from aocd import get_data
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f655fd2e595cba5948c90062751ec15cc76678cb3f4c35a987b10ec7758ffa7c3185a01dd7136706083020407fcb659b0fbc22a4277a0fa53"
q = get_data(day=5, year=2022)
print(f"[{q}]")