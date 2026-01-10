class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipeMap = {}
        for i, recipe in enumerate(recipes):
            ingredientsForRecipe = ingredients[i]
            recipeMap[recipe] = ingredientsForRecipe
        #print(recipeMap)

        output = set()
        availableSupplies = set(supplies)
        visited = set()
        #print(availableSupplies)
        def dfsCanMakeRecipe(recipe) -> bool:
            if recipe in visited:
                return False

            deps = recipeMap[recipe]
            if len(deps) == 0:
                return True
            
            visited.add(recipe)
            for dep in deps:
                if dep in recipeMap and not dfsCanMakeRecipe(dep):
                    return False
                
                if dep not in recipeMap and dep not in availableSupplies:
                    return False

            visited.remove(recipe)
            recipeMap[recipe] = []
            output.add(recipe)

            return True

        for recipe in recipes:
            if not dfsCanMakeRecipe(recipe):
                continue


        return [ recipe for recipe in output ]
