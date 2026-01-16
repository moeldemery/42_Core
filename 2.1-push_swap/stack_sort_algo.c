/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_sort_algo.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/10 23:34:43 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/10 23:34:45 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_sort_three(td_list **stack)
{
	int			first;
	int			second;
	int			third;
	t_element	*elem;

	first = ((t_element *)(*stack)->content)->value;
	second = ((t_element *)(*stack)->next->content)->value;
	third = ((t_element *)(*stack)->next->next->content)->value;
	if (first > second && second < third && first < third)
		ft_sa(stack);
	else if (first > second && second > third)
	{
		ft_sa(stack);
		ft_rra(stack);
	}
	else if (first > second && second < third && first > third)
		ft_ra(stack);
	else if (first < second && second > third && first < third)
	{
		ft_sa(stack);
		ft_ra(stack);
	}
	else if (first < second && second > third && first > third)
		ft_ra(stack);
}

void	ft_sort_four(td_list **stack_a, td_list **stack_b)
{
	int	pos;

	if (ft_is_sorted(*stack_a) == 1)
		return ;
	pos = ft_find_min(*stack_a, DEBUG);
	if (pos == 1)
		ft_ra(stack_a);
	else if (pos == 2)
	{
		ft_ra(stack_a);
		ft_ra(stack_a);
	}
	else if (pos == 3)
		ft_rra(stack_a);
	ft_pb(stack_a, stack_b);
	ft_sort_three(stack_a);
	ft_pa(stack_a, stack_b);
}

void	ft_sort_five(td_list **stack_a, td_list **stack_b)
{
	int	pos;

	if (ft_is_sorted(*stack_a) == 1)
		return ;
	pos = ft_find_min(*stack_a, DEBUG);
	if (pos == 1)
		ft_ra(stack_a);
	else if (pos == 2)
	{
		ft_ra(stack_a);
		ft_ra(stack_a);
	}
	else if (pos == 3)
	{
		ft_rra(stack_a);
		ft_rra(stack_a);
	}
	else if (pos == 4)
		ft_rra(stack_a);
	ft_pb(stack_a, stack_b);
	ft_sort_four(stack_a, stack_b);
	ft_pa(stack_a, stack_b);
}

void	ft_sort_n(td_list **stack_a, td_list **stack_b, int size)
{
	int	lis_len;

	lis_len = ft_find_lis(stack_a, size);
	ft_list_print_lismask(*stack_a, (int)DEBUG, "Final  LIS Mask:");
	ft_push_non_lis(stack_a, stack_b, size, lis_len);
	ft_list_print(*stack_a, (int)DEBUG, "LIS Stack A:");
	ft_list_print(*stack_b, (int)DEBUG, "LIS Stack B:");
	ft_sort_remaining(stack_a, stack_b);
	ft_final_rotate(stack_a);
}

int	ft_sort_stack(td_list **stack_a, td_list **stack_b)
{
	int	size;

	size = ft_lstd_size(*stack_a);
	if (size <= 1 || ft_is_sorted(*stack_a))
		return (0);
	else if (size == 2)
	{
		if (*(int *)(*stack_a)->content > *(int *)(*stack_a)->next->content)
			ft_sa(stack_a);
	}
	else if (size == 3)
		ft_sort_three(stack_a);
	else if (size == 4)
		ft_sort_four(stack_a, stack_b);
	else if (size == 5)
		ft_sort_five(stack_a, stack_b);
	else
		ft_sort_n(stack_a, stack_b, size);
	ft_list_print(*stack_a, (int)DEBUG, "Sorted Stack A:");
	ft_list_print(*stack_b, (int)DEBUG, "Sorted Stack B:");
	return (0);
}
