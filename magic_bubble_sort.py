def magic_bubble_sort(nums: list[int]):
    """魔法冒泡排序算法，默认偶数比奇数大
    :param nums: 需要排序的数组，函数会直接修改原始数组
    :return: 从小到大排序后的数组
    """
    iteration_count = len(nums) - 1
    while iteration_count > 0:
        for i in range(iteration_count):
            current, next_ = nums[i], nums[i + 1]
            is_current_even, is_next_even = current % 2 == 0, next_ % 2 == 0
            # 是否需要将“大”的数换到右边:
            # 左偶右奇 or (左右奇偶相等 and 左大右小)
            should_swap = False
            if is_current_even and not is_next_even:
                should_swap = True
            elif is_current_even == is_next_even and current > next_:
                should_swap = True

            if should_swap:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

        iteration_count -= 1
