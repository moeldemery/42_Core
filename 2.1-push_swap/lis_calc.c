/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   lis_calc.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/15 01:14:30 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/15 01:14:32 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

static void	ft_update_lis_cost(t_element *curr_elem, t_element *prev_elem)
{
	if (curr_elem->value > prev_elem->value)
	{
		if (curr_elem->lis_cost < prev_elem->lis_cost + 1)
			curr_elem->lis_cost = prev_elem->lis_cost + 1;
	}
}

static int	ft_process_lis_element(td_list *stack_a, td_list *curr)
{
	td_list		*prev;
	t_element	*curr_elem;
	int			max_update;

	max_update = 1;
	curr_elem = (t_element *)curr->content;
	prev = stack_a;
	while (prev != curr)
	{
		ft_update_lis_cost(curr_elem, (t_element *)prev->content);
		prev = prev->next;
	}
	if (curr_elem->lis_cost > max_update)
		max_update = curr_elem->lis_cost;
	return (max_update);
}

int	ft_calculate_lis(td_list **stack_a, int size)
{
	td_list		*curr;
	int			max_len;

	if (size <= 1)
		return (size);
	max_len = 1;
	curr = (*stack_a)->next;
	while (curr)
	{
		if (ft_process_lis_element(*stack_a, curr) > max_len)
			max_len = ((t_element *)curr->content)->lis_cost;
		curr = curr->next;
	}
	return (max_len);
}
