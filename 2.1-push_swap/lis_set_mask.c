/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   lis_set_mask.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/15 21:26:01 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/15 21:26:06 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	ft_find_predecessor(td_list *stack_a, td_list *curr,
		int current_needed, int elem_value)
{
	td_list		*check;
	t_element	*check_elem;

	check = stack_a;
	while (check != curr)
	{
		check_elem = (t_element *)check->content;
		if (check_elem->lis_cost == current_needed - 1
			&& check_elem->value < elem_value)
			return (1);
		check = check->next;
	}
	return (0);
}

static void	ft_mark_lis_element(td_list *elem, int *current_needed,
		int *last_value)
{
	t_element	*elem_data;

	elem_data = (t_element *)elem->content;
	elem_data->lis_mask = 1;
	*last_value = elem_data->value;
	(*current_needed)--;
}

void	ft_set_max_lis_mask(td_list *stack_a, int max_len)
{
	td_list		*temp;
	int			current_needed;
	int			last_value;
	t_element	*elem;

	current_needed = max_len;
	last_value = MAX_INT;
	temp = ft_lstd_last(stack_a);
	while (temp && current_needed > 0)
	{
		elem = (t_element *)temp->content;
		if (elem->lis_cost == current_needed && elem->value < last_value)
		{
			if (current_needed == 1 || ft_find_predecessor(stack_a, temp,
					current_needed, elem->value))
				ft_mark_lis_element(temp, &current_needed, &last_value);
		}
		temp = temp->prev;
	}
}
