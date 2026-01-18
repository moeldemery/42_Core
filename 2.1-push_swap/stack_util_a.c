/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_util_a.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/12 15:02:46 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/12 15:02:48 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_is_str_digit(char *str)
{
	int	i;

	i = 0;
	if (str[i] == '-' || str[i] == '+')
		i++;
	while (str[i])
	{
		if (ft_isdigit(str[i]) == 0)
			return (0);
		i++;
	}
	return (1);
}

t_element	*ft_init_element(int value)
{
	t_element	*element;

	element = malloc(sizeof(t_element));
	if (!element)
		return (NULL);
	element->value = value;
	element->cost = 0;
	element->lis_cost = 1;
	element->lis_mask = 0;
	return (element);
}

int	ft_is_sorted(t_d_list *stack)
{
	t_d_list	*current;
	t_element	*curr_elem;
	t_element	*next_elem;

	current = stack;
	while (current && current->next)
	{
		curr_elem = (t_element *)current->content;
		next_elem = (t_element *)current->next->content;
		if (curr_elem->value > next_elem->value)
			return (0);
		current = current->next;
	}
	return (1);
}

int	ft_find_min(t_d_list *stack, int is_debug)
{
	t_d_list	*temp;
	int			index;
	int			min;
	int			pos;
	t_element	*elem;

	if (!stack)
		return (-1);
	temp = stack;
	index = 0;
	min = ((t_element *)temp->content)->value;
	while (temp)
	{
		elem = (t_element *)temp->content;
		if (elem->value < min)
		{
			min = elem->value;
			pos = index;
		}
		temp = temp->next;
		index++;
	}
	if (is_debug != 0)
		ft_printf("Minimum value in stack is %d at position %d\n", min, pos);
	return (pos);
}

int	ft_find_max(t_d_list *stack, int is_debug)
{
	t_d_list	*temp;
	int			index;
	int			max;
	int			pos;
	t_element	*elem;

	if (!stack)
		return (-1);
	temp = stack;
	index = 0;
	max = ((t_element *)temp->content)->value;
	while (temp)
	{
		elem = (t_element *)temp->content;
		if (elem->value > max)
		{
			max = elem->value;
			pos = index;
		}
		temp = temp->next;
		index++;
	}
	if (is_debug)
		ft_printf("Maximum value in stack is %d at position %d\n", max, pos);
	return (pos);
}
