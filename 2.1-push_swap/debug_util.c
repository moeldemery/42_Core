/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   debug_util.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/14 15:36:05 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/14 15:36:08 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_list_print(td_list *lst, int is_enabled, char *msg)
{
	td_list		*temp;
	t_element	*elem;

	if (is_enabled == 0)
		return (0);
	if (msg)
		ft_printf("%s\n[ ", msg);
	temp = lst;
	while (temp)
	{
		elem = (t_element *)temp->content;
		ft_printf("%d\t", elem->value);
		temp = temp->next;
	}
	ft_printf("]\n");
	return (1);
}

int	ft_list_print_liscost(td_list *lst, int is_enabled, char *msg)
{
	td_list		*temp;
	t_element	*elem;

	if (is_enabled == 0)
		return (0);
	if (msg)
		ft_printf("%s [ ", msg);
	temp = lst;
	while (temp)
	{
		elem = (t_element *)temp->content;
		ft_printf("%d ", elem->lis_cost);
		temp = temp->next;
	}
	ft_printf("]\n");
	return (1);
}

int	ft_list_print_lismask(td_list *lst, int is_enabled, char *msg)
{
	td_list		*temp;
	t_element	*elem;

	if (is_enabled == 0)
		return (0);
	if (msg)
		ft_printf("%s [ ", msg);
	temp = lst;
	while (temp)
	{
		elem = (t_element *)temp->content;
		ft_printf("%d ", elem->lis_mask);
		temp = temp->next;
	}
	ft_printf("]\n");
	return (1);
}

int	ft_list_print_costs(td_list *lst, int is_enabled, char *msg)
{
	td_list		*temp;
	t_element	*elem;

	if (is_enabled == 0)
		return (0);
	if (msg)
		ft_printf("%s\n[ ", msg);
	temp = lst;
	while (temp)
	{
		elem = (t_element *)temp->content;
		ft_printf("%d ", elem->cost);
		temp = temp->next;
	}
	ft_printf("]\n");
	return (1);
}

int	ft_print_index_costs(td_list *lst,int index, int is_enabled, char *msg)
{
	td_list		*temp;
	t_element	*elem;

	if (is_enabled == 0)
		return (0);
	if (msg)
		ft_printf("%s\n[ ", msg);
	temp = lst;
	while (temp && index-- > 0)
		temp = temp->next;
	if (temp)
	{
		elem = (t_element *)temp->content;
		ft_printf("%d ", elem->cost);
	}
	ft_printf("]\n");
	return (1);
}