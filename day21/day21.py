from common.common import get_lines


class FoodWithAllergens:
    def __init__(self, line):
        ing, alg = line.replace(')', '').split(' (contains ')
        self.ingredients, self.allergens = ing.split(' '), alg.split(', ')


if __name__ == '__main__':
    food_lines = [FoodWithAllergens(x) for x in get_lines('in.txt')]
    ing_set = set(x for food_line in food_lines for x in food_line.ingredients)
    alg_set = set(x for food_line in food_lines for x in food_line.allergens)

    # part 1
    possible_reason = {}
    safe_ings = ing_set
    for alg in alg_set:
        possible_reason[alg] = ing_set
        for food_line in food_lines:
            if alg in food_line.allergens:
                possible_reason[alg] = possible_reason[alg] & set(food_line.ingredients)
        safe_ings = safe_ings - possible_reason[alg]
    print(sum(1 for safe_ing in safe_ings for food_line in food_lines if safe_ing in food_line.ingredients))

    # part 2
    while not all([len(x) == 1 for x in possible_reason.values()]):
        next_vals = [x for x in possible_reason.values() if len(x) == 1]
        for next_val in next_vals:
            for ing in possible_reason.values():
                if len(next_val & ing) == 1 and len(ing) != 1:
                    ing.difference_update(next_val)
    print(','.join(list(possible_reason[x])[0] for x in sorted(possible_reason)))
