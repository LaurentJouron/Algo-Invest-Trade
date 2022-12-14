import csv


class DataList:
    @staticmethod
    def get_data_from_csv(self):
        """
        This function reads the .csv file, stock the items in a list and
        return it.
        :param:
            str: csv_name
        :return:
            list: actions_list without fieldnames [name, cost, profit]
            """
        csv_to_list: list = []
        with open(f'data/data_file/{self}.csv', newline='') as csvfile:
            actions = csv.reader(csvfile, delimiter=',')
            csv_to_list.extend(iter(actions))
            return csv_to_list[1:]

    @staticmethod
    def add_performance(actions):
        """
        Calculation the best percentage of profitability.
        :param:
            list: action_list [name, cost, profit, performance]
        :return:
            list: action_list with 4 items [name, cost, profit, performance]
        """
        action_list: list = []
        for i in range(len(actions)):
            if float(actions[i][2]) > 0.0 and float(actions[i][1]) > 0.0:
                performance = float(actions[i][2]) / 100 * float(actions[i][1])
                action_list.append([actions[i][0], float(actions[i][1]),
                                    float(actions[i][2]),
                                    round(performance, 2)])
        return action_list

    @staticmethod
    def sort_on_performance(performance):
        """
        Sorts the results of each action in descending order.
        :param:
            list: list with performance [name, cost, profit, performance]
        :return:
            list: sort_list on performance
        """
        return sorted(performance, key=lambda x: x[3], reverse=True)

    @staticmethod
    def get_cost_invest(actions_list):
        """
        By passing a list in parameter we obtain its investment cost.
        :param:
            list: action_list [name, cost, profit, performance]
        :return:
            float: cost_invest
        """
        cost: float = 0.0
        for i in range(len(actions_list)):
            cost += actions_list[i][1]
        return cost

    @staticmethod
    def get_profit(actions_list):
        """
        By passing a list as a parameter we obtain its best profitability
        :param:
            list: action_list [name, cost, profit, performance]
        :return:
            float: profitability
        """
        profit: float = 0.0
        for i in range(len(actions_list)):
            profit += actions_list[i][3]
        return profit
