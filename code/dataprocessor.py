class DataProcessor():

    def __init__(self):
        pass

    def parse_csv_contents(self, contents: str) -> list[str]:
        pass

    def handle_investment(self, principal: float, interest_rate: float, time_period: int, type: str) -> float:
        pass

    #Calculates simple interest
    def simple_interest(self, principal, interest_rate, time_period):
        """
            Args:
                principal: Initial amount invested.
                interest_rate: Annual interest rate as a decimal
                time_period: Time since investment (e.g., daily, monthly, quarterly, annually)

            Returns:
                Calculated simple interest.
        """

        if time_period == 'daily':
            time_period = 1 / 365.25
        elif time_period == 'monthly':
            time_period = 1 / 12
        elif time_period == 'quarterly':
            time_period = 1 / 4
        elif time_period == 'annually':
            time_period = 1
        else:
            print("Invalid time period")
            return

        #simple interest calculation
        interest = (principal * interest_rate * time_period) /100
        #simplify to two decimal places
        interest = round(interest, 2)
        
        return interest
    
    def compound_interest(self, principal, interest_rate, time_period):
        """
            Args:
                principal: Initial amount invested.
                interest_rate: Annual interest rate as a decimal
                time_period: Time since investment (e.g., daily, monthly, quarterly, annually)

            Returns:
                Calculated compound interest.
        """

        if time_period == 'daily':
            n = 365.25
        elif time_period == 'monthly':
            n = 12
        elif time_period == 'quarterly':
            n = 4
        elif time_period == 'annually':
            n = 1
        else:
            print("Invalid time period")
            return
        
        #Calculate compound interest over the course of 1 year
        #A = final amount 
        t = 1
        A = principal * (1 + interest_rate/n)**(n*t)
        interest = A - principal
        #Simplify to two decimal places
        interest = round(interest, 2)
        
        return interest