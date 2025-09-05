import allure

def test_nested_steps_depth_10():
    def nested_step(level, max_depth):
        with allure.step(f"Step level {level}"):
            if level < max_depth:
                nested_step(level + 1, max_depth)

    nested_step(1, 10) 