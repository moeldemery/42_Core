/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/10 14:34:49 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/10 14:34:52 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

int	ft_is_str_digit(char *str)
{
	int	i;

	i = 0;
	if (str[i] == '-' || str[i] == '+')
		i++;
	while (str[i])
	{
		if (ft_isdigit(str[i]) == 0)
			return (0);
		i++;
	}
	return (1);
}

t_element	*ft_init_element(int value)
{
	t_element	*element;

	element = malloc(sizeof(t_element));
	if (!element)
		return (NULL);
	element->value = value;
	element->cost = 0;
	element->lis_cost = 1;
	element->lis_mask = 0;
	return (element);
}

static int	ft_process_arg(char *arg, td_list **stack)
{
	t_element	*element;
	int			num;

	if (ft_is_str_digit(arg) == 0)
		return (0);
	num = ft_atoi(arg);
	element = ft_init_element(num);
	ft_lstd_add_back(stack, ft_lstd_new(element));
	return (1);
}

static int	ft_proccess_arg_split(char *arg, td_list **stack)
{
	t_element	*element;
	int			num;
	char		**args_split;
	char		**args_ptr;

	args_split = ft_split(arg, ' ');
	if (!args_split)
		return (ft_printf("Error\n") != 0);
	args_ptr = args_split;
	while (*args_split)
	{
		if (ft_is_str_digit(*args_split) == 0)
		{
			free(args_ptr);
			return (ft_printf("Error\n") != 0);
		}
		num = ft_atoi(*args_split);
		element = ft_init_element(num);
		ft_lstd_add_back(stack, ft_lstd_new(element));
		args_split++;
	}
	free(args_ptr);
	return (1);
}

int	main(int argc, char **argv)
{
	td_list	*stack_a;
	td_list	*stack_b;
	int		i;

	stack_a = NULL;
	stack_b = NULL;
	i = 1;
	if (argc == 2)
	{
		if (!ft_proccess_arg_split(argv[1], &stack_a))
			return (ft_printf("Error\n") != 0);
		ft_list_print(stack_a, DEBUG, "Initial Stack A:");
		ft_list_print(stack_b, DEBUG, "Initial Stack B:");
		return (ft_sort_stack(&stack_a, &stack_b));
	}
	else if (argc > 2)
	{
		while (i < argc)
		{
			if (!ft_process_arg(argv[i], &stack_a))
				return (ft_printf("Error\n") != 0);
			i++;
		}
		ft_list_print(stack_a, DEBUG, "Initial Stack A:");
		ft_list_print(stack_b, DEBUG, "Initial Stack B:");
		return (ft_sort_stack(&stack_a, &stack_b));
	}
	else
		return (ft_printf("Error\n") != 0);
}
