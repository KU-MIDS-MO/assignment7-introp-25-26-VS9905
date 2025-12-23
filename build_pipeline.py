def build_pipeline(operation_names):

    for i in operation_names:
        if i not in ["double", "triple", "square"]:
            raise KeyError("Operation not recognized.")


    def pipeline(x):
        result = x

        for i in operation_names:
            if i == "double":
                result = result * 2
            elif i == "triple":
                result = result * 3
            elif i == "square":
                result = result ** 2

        return result

    return pipeline


