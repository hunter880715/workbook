# coding: GBK 
def print_models(unprinted_designs, completed_models):
    """
    ģ���ӡÿ����ƣ�ֱ��û��δ��ӡ�����Ϊֹ
    ��ӡÿ����ƺ󣬶������ƶ����б�completed_models��
    """
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        """ģ��������������ӡģ�͵Ĺ���"""
        print("printing model: " + current_designs)
        completed_models.append(current_designs)

def show_completed_models(completed_models):
    """��ʾ��ӡ�õ�����ģ��"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

