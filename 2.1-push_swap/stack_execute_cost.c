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

t_d_list	*ft_get_element_at_index(t_d_list *stack, int index)
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

static void	ft_apply_double_rotations(t_d_list **a, t_d_list **b,
		t_element *best)
{
	while (best->cost_a > 0 && best->cost_b > 0)
	{
		ft_rr(a, b, 1);
		best->cost_a--;
		best->cost_b--;
	}
	while (best->cost_a < 0 && best->cost_b < 0)
	{
		ft_rrr(a, b, 1);
		best->cost_a++;
		best->cost_b++;
	}
}

static void	ft_apply_single_a(t_d_list **a, t_element *best)
{
	while (best->cost_a > 0)
	{
		ft_ra(a, 1);
		best->cost_a--;
	}
	while (best->cost_a < 0)
	{
		ft_rra(a, 1);
		best->cost_a++;
	}
}

static void	ft_apply_single_b(t_d_list **b, t_element *best)
{
	while (best->cost_b > 0)
	{
		ft_rb(b, 1);
		best->cost_b--;
	}
	while (best->cost_b < 0)
	{
		ft_rrb(b, 1);
		best->cost_b++;
	}
}

void	ft_execute_cheapest_move(t_d_list **stack_a, t_d_list **stack_b)
{
	t_element	*best;
	int			best_idx;
	t_d_list	*best_node;

	best_idx = ft_find_cheapest_index(*stack_b);
	best_node = ft_get_element_at_index(*stack_b, best_idx);
	if (!best_node)
		return ;
	best = (t_element *)best_node->content;
	ft_apply_double_rotations(stack_a, stack_b, best);
	ft_apply_single_a(stack_a, best);
	ft_apply_single_b(stack_b, best);
	ft_pa(stack_a, stack_b, 1);
}
