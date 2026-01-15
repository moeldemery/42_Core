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

int	ft_get_combined_cost(int a, int b)
{
	int	abs_a;
	int	abs_b;

	if (a >= 0 && b >= 0)
	{
		if (a > b)
			return (a);
		return (b);
	}
	if (a < 0 && b < 0)
	{
		abs_a = -a;
		abs_b = -b;
		if (abs_a > abs_b)
			return (abs_a);
		return (abs_b);
	}
	if (a < 0)
		abs_a = -a;
	else
		abs_a = a;
	if (b < 0)
		abs_b = -b;
	else
		abs_b = b;
	return (abs_a + abs_b);
}

void	ft_calculate_costs(td_list **stack_a, td_list **stack_b, int size_a, int size_b)
{
	td_list		*temp_b;
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