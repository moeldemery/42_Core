/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_calculate_cost.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/15 08:18:34 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/15 08:18:36 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	ft_reset_costs(t_d_list *stack_b)
{
	t_element	*el;

	while (stack_b)
	{
		el = (t_element *)stack_b->content;
		el->cost_a = 0;
		el->cost_b = 0;
		el->cost = 0;
		stack_b = stack_b->next;
	}
}

static int	ft_abs(int n)
{
	if (n < 0)
		return (-n);
	return (n);
}

static int	ft_same_direction_cost(int a, int b)
{
	if (a >= 0 && b >= 0)
	{
		if (a > b)
			return (a);
		return (b);
	}
	if (ft_abs(a) > ft_abs(b))
		return (ft_abs(a));
	return (ft_abs(b));
}

int	ft_get_combined_cost(int a, int b)
{
	if ((a >= 0 && b >= 0) || (a < 0 && b < 0))
		return (ft_same_direction_cost(a, b));
	return (ft_abs(a) + ft_abs(b));
}

void	ft_calculate_costs(t_d_list **stack_a, t_d_list **stack_b, int size_a,
		int size_b)
{
	t_d_list	*temp_b;
	t_element	*el;
	int			i_b;
	int			pos_a;

	temp_b = *stack_b;
	i_b = 0;
	while (temp_b)
	{
		el = (t_element *)temp_b->content;
		pos_a = ft_find_insert_position(*stack_a, el->value);
		if (pos_a <= size_a / 2)
			el->cost_a = pos_a;
		else
			el->cost_a = pos_a - size_a;
		if (i_b <= size_b / 2)
			el->cost_b = i_b;
		else
			el->cost_b = i_b - size_b;
		el->cost = ft_get_combined_cost(el->cost_a, el->cost_b);
		temp_b = temp_b->next;
		i_b++;
	}
}
