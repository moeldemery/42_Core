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

int	main(int argc, char **argv)
{
	t_d_list	*stack_a;
	t_d_list	*stack_b;
	int			i;

	stack_a = NULL;
	stack_b = NULL;
	i = 1;
	if (argc == 2)
	{
		if (!ft_proccess_arg_split(argv[1], &stack_a))
			return (ft_printf("Error\n") != 0);
	}
	else if (argc > 2)
	{
		while (i++ < argc - 1)
			if (!ft_process_arg(argv[i], &stack_a))
				return (free_stack(&stack_a), ft_printf("Error\n"), 1);
	}
	else
		return (ft_printf("Error\n") != 0);
	ft_list_print(stack_a, DEBUG, "Initial Stack A:");
	ft_list_print(stack_b, DEBUG, "Initial Stack B:");
	return (ft_sort_stack(&stack_a, &stack_b));
}
