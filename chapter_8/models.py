# coding: GBK 
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移动到列表completed_models中
    """
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        """模拟根据设计制作打印模型的过程"""
        print("printing model: " + current_designs)
        completed_models.append(current_designs)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

