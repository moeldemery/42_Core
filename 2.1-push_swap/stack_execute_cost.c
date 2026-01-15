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

/*
static void	ft_rotate_forward(td_list **stack_a, td_list **stack_b,
		int best_index, int insert_pos)
{
	int	min_rot;
	int	i;

	if (best_index < insert_pos)
		min_rot = best_index;
	else
		min_rot = insert_pos;
	i = -1;
	while (++i < min_rot)
		ft_rr(stack_a, stack_b);
	while (best_index-- > min_rot)
		ft_rb(stack_b);
}

static void	ft_rotate_backward(td_list **stack_a, td_list **stack_b,
		int best_index, int insert_pos)
{
	int	min_rot;
	int	i;
	int	size_a;

	size_a = ft_lstd_size(*stack_a);
	if (best_index < size_a - insert_pos)
		min_rot = best_index;
	else
		min_rot = size_a - insert_pos;
	i = -1;
	while (++i < min_rot)
		ft_rrr(stack_a, stack_b);
	while (best_index-- > min_rot)
		ft_rrb(stack_b);
}

static void	ft_rotate_to_cheapest(td_list **stack_a, td_list **stack_b,
		int best_index, int insert_pos)
{
	int	size_a;

	size_a = ft_lstd_size(*stack_a);
	if (best_index <= 0)
		return ;
	if (insert_pos <= size_a / 2)
		ft_rotate_forward(stack_a, stack_b, best_index, insert_pos);
	else
		ft_rotate_backward(stack_a, stack_b, best_index, insert_pos);
}

static void	ft_insert_and_push(td_list **stack_a, td_list **stack_b)
{
	int	insert_pos;
	int	size_a;
	int	i;

	size_a = ft_lstd_size(*stack_a);
	insert_pos = ft_find_insert_position(*stack_a,
			((t_element *)(*stack_b)->content)->value);
	i = 0;
	if (insert_pos <= size_a / 2)
		while (i++ < insert_pos)
			ft_ra(stack_a);
	else
		while (i++ < size_a - insert_pos)
			ft_rra(stack_a);
	ft_pa(stack_a, stack_b);
}

void	ft_execute_cheapest_move(td_list **stack_a, td_list **stack_b)
{
	int	best_index;
	int	insert_pos;

	if (ft_lstd_size(*stack_b) == 0)
		return ;
	best_index = ft_find_cheapest_index(*stack_b);
	insert_pos = ft_find_insert_position(*stack_a,
			((t_element *)(*stack_b)->content)->value);
	ft_rotate_to_cheapest(stack_a, stack_b, best_index, insert_pos);
	ft_insert_and_push(stack_a, stack_b);
}
*/
td_list	*ft_get_element_at_index(td_list *stack, int index)
{
	int	i;

	i = 0;
	if (!stack)
		return (NULL);
	while (stack != NULL)
	{
		if (i == index)
			return (stack);
		stack = stack->next;
		i++;
	}
	return (NULL);
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

	best_idx = ft_find_cheapest_index(*stack_b);
	best = (t_element *)ft_get_element_at_index(*stack_b, best_idx)->content;
	ft_apply_double_rotations(stack_a, stack_b, best);
	ft_apply_single_a(stack_a, best);
	ft_apply_single_b(stack_b, best);
	ft_pa(stack_a, stack_b);
}
