/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_util_b.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/12 17:01:53 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/12 17:02:01 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_find_min_index(td_list *stack)
{
	int		min_idx;
	int		i;
	int		min_val;
	td_list	*curr;

	if (!stack)
		return (0);
	curr = stack;
	min_val = ((t_element *)curr->content)->value;
	min_idx = 0;
	i = 0;
	while (curr)
	{
		if (((t_element *)curr->content)->value < min_val)
		{
			min_val = ((t_element *)curr->content)->value;
			min_idx = i;
		}
		curr = curr->next;
		i++;
	}
	return (min_idx);
}

int	ft_find_insert_position(td_list *stack_a, int value)
{
	td_list		*curr;
	int			target_idx;
	int			closest_bigger;
	int			i;
	t_element	*el;

	closest_bigger = MAX_INT;
	target_idx = ft_find_min_index(stack_a);
	curr = stack_a;
	i = 0;
	while (curr)
	{
		el = (t_element *)curr->content;
		if (el->value > value && el->value < closest_bigger)
		{
			closest_bigger = el->value;
			target_idx = i;
		}
		curr = curr->next;
		i++;
	}
	return (target_idx);
}

int	ft_find_cheapest_index(td_list *stack_b)
{
	td_list		*temp_b;
	t_element	*elem;
	int			min_cost;
	int			best_index;
	int			current_index;

	min_cost = MAX_INT;
	best_index = -1;
	current_index = 0;
	temp_b = stack_b;
	while (temp_b != NULL)
	{
		elem = (t_element *)temp_b->content;
		if (elem->cost < min_cost)
		{
			min_cost = elem->cost;
			best_index = current_index;
		}
		temp_b = temp_b->next;
		current_index++;
	}
	return (best_index);
}
