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

int	ft_find_insert_position(td_list *stack_a, int value)
{
	td_list		*temp;
	int			position;
	t_element	*elem;
	t_element	*next_elem;
	t_element	*last_elem;

	temp = stack_a;
	position = 0;
	if (!stack_a || !stack_a->next)
    	return (0);
	while (temp->next != NULL)
	{
		elem = (t_element *)temp->content;
		next_elem = (t_element *)temp->next->content;
		if (value > elem->value && value < next_elem->value)
			return (position + 1);
		temp = temp->next;
		position++;
	}
	last_elem = (t_element *)temp->content;
	if (value > last_elem->value)
		return (position + 1);
	return (0);
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
