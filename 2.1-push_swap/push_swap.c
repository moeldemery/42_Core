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

static void	ft_error_exit(t_d_list **stack)
{
	free_stack(stack);
	write(2, "Error\n", 6);
	exit(1);
}

int	main(int argc, char **argv)
{
	t_d_list	*stack_a;
	t_d_list	*stack_b;
	int			i;

	stack_a = NULL;
	stack_b = NULL;
	i = 1;
	if (argc < 2)
		return (0);
	while (i < argc)
	{
		if (ft_strchr(argv[i], ' '))
		{
			if (!ft_proccess_arg_split(argv[i], &stack_a))
				ft_error_exit(&stack_a);
		}
		else
			if (!ft_process_arg(argv[i], &stack_a))
				ft_error_exit(&stack_a);
		i++;
	}
	ft_list_print(stack_a, DEBUG, "Initial Stack A:");
	ft_list_print(stack_b, DEBUG, "Initial Stack B:");
	return (ft_sort_stack(&stack_a, &stack_b));
}
