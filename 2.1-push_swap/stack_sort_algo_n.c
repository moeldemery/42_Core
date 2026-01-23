/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_sort_algo_n.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/14 23:05:08 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/14 23:05:10 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_find_lis(t_d_list **stack_a, int size)
{
	int	lis_len;

	if (size == 0)
		return (0);
	lis_len = ft_calculate_lis(stack_a, size);
	ft_list_print_liscost(*stack_a, DEBUG, "Initial LIS Cost:");
	ft_set_max_lis_mask(*stack_a, lis_len);
	ft_list_print_lismask(*stack_a, DEBUG, "Current LIS Mask:");
	return (lis_len);
}

void	ft_push_non_lis(t_d_list **stack_a, t_d_list **stack_b, int size,
		int lis_len)
{
	int			pushed;
	int			limit;
	t_element	*elem;

	pushed = 0;
	limit = size - lis_len;
	while (pushed < limit)
	{
		elem = (t_element *)(*stack_a)->content;
		if (elem->lis_mask == 0)
		{
			ft_pb(stack_a, stack_b, 1);
			pushed++;
		}
		else
			ft_ra(stack_a, 1);
	}
}

void	ft_sort_remaining(t_d_list **stack_a, t_d_list **stack_b)
{
	int	size_a;
	int	size_b;

	size_a = ft_lstd_size(*stack_a);
	size_b = ft_lstd_size(*stack_b);
	while (*stack_b)
	{
		ft_reset_costs(*stack_b);
		size_a = ft_lstd_size(*stack_a);
		size_b = ft_lstd_size(*stack_b);
		ft_calculate_costs(stack_a, stack_b, size_a, size_b);
		ft_list_print_costs(*stack_a, DEBUG, "Costs in Stack A:");
		ft_list_print_costs(*stack_b, DEBUG, "Costs in Stack B:");
		ft_execute_cheapest_move(stack_a, stack_b);
	}
}

void	ft_final_rotate(t_d_list **stack_a)
{
	int	min_pos;
	int	size_a;

	size_a = ft_lstd_size(*stack_a);
	min_pos = ft_find_min(*stack_a, DEBUG);
	if (min_pos <= size_a / 2)
	{
		while (min_pos-- > 0)
			if (!ft_is_sorted(*stack_a))
				ft_ra(stack_a, 1);
	}
	else
	{
		while (size_a - min_pos++ > 0)
			if (!ft_is_sorted(*stack_a))
				ft_rra(stack_a, 1);
	}
}
