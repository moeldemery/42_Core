/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_execute_cost.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/15 01:36:12 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/15 01:36:13 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

td_list	*ft_get_element_at_index(td_list *stack, int index)
{
	if (!stack || index < 0)
		return (NULL);
	while (stack && index > 0)
	{
		stack = stack->next;
		index--;
	}
	return (stack);
}

static void	ft_apply_double_rotations(td_list **a, td_list **b, t_element *best)
{
	while (best->cost_a > 0 && best->cost_b > 0)
	{
		ft_rr(a, b);
		best->cost_a--;
		best->cost_b--;
	}
	while (best->cost_a < 0 && best->cost_b < 0)
	{
		ft_rrr(a, b);
		best->cost_a++;
		best->cost_b++;
	}
}

static void	ft_apply_single_a(td_list **a, t_element *best)
{
	while (best->cost_a > 0)
	{
		ft_ra(a);
		best->cost_a--;
	}
	while (best->cost_a < 0)
	{
		ft_rra(a);
		best->cost_a++;
	}
}

static void	ft_apply_single_b(td_list **b, t_element *best)
{
	while (best->cost_b > 0)
	{
		ft_rb(b);
		best->cost_b--;
	}
	while (best->cost_b < 0)
	{
		ft_rrb(b);
		best->cost_b++;
	}
}

void	ft_execute_cheapest_move(td_list **stack_a, td_list **stack_b)
{
	t_element	*best;
	int			best_idx;
	td_list		*best_node;

	best_idx = ft_find_cheapest_index(*stack_b);
	best_node = ft_get_element_at_index(*stack_b, best_idx);
	if (!best_node)
		return ;
	best = (t_element *)best_node->content;
	ft_apply_double_rotations(stack_a, stack_b, best);
	ft_apply_single_a(stack_a, best);
	ft_apply_single_b(stack_b, best);
	ft_pa(stack_a, stack_b);
}
