

with open("input.txt") as f:
    lines = f.readlines()
    job_pairs = [item.replace("\n", "") for item in lines]

fully_overlapping_sections = 0
partially_overlapping_sections = 0

for job_pair in job_pairs:
    job_pair_split = job_pair.split(",")
    elf_1 = job_pair_split[0].split("-")
    elf_2 = job_pair_split[1].split("-")

    elf_1_sections = list(range(int(elf_1[0]), int(elf_1[1])+1, 1))
    elf_2_sections = list(range(int(elf_2[0]), int(elf_2[1])+1, 1))

    overlapping_sections = list(set(elf_1_sections) & set(elf_2_sections))
    overlapping_sections.sort()

    if overlapping_sections == elf_1_sections or overlapping_sections == elf_2_sections:
        fully_overlapping_sections += 1

    if len(overlapping_sections) > 0:
        partially_overlapping_sections += 1

part_1_answer = fully_overlapping_sections
print(part_1_answer)

part_2_answer = partially_overlapping_sections
print(part_2_answer)
